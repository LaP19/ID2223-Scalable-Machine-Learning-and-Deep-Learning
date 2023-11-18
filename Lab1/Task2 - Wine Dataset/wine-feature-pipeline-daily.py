import modal
import numpy as np
import hopsworks
import pandas as pd

LOCAL=False #to run it in modal we have to set LOCAL to false --> to run it into terminal: modal run ... + modal deploy to make it run everyday

if LOCAL == False:
   stub = modal.Stub("wine_daily")
   image = modal.Image.debian_slim().pip_install(["hopsworks"])

   @stub.function(image=image, schedule=modal.Period(minutes=5), secret=modal.Secret.from_name("HOPSWORKS_API_KEY"))
   def f():
       g()


project = hopsworks.login()
fs = project.get_feature_store()

wine_fg = fs.get_feature_group(name="wine_reduced_new", version=1)
wine_df = wine_fg.read()
print(wine_df)
def generate_sample_for_quality(df, deviation_factor=0.1):
    sample = {}
    wine_types = [0, 1]
    quality_score = [3,4,5,6,7,8,9]
    quality_score = np.random.choice(quality_score)
    selected_type = np.random.choice(wine_types)
    while (quality_score == 9 and selected_type == 1):
        quality_score = np.random.choice(quality_score)
        selected_type = np.random.choice(wine_types)

    quality_type_df = df[(df['quality'] == quality_score) & (df['type'] == selected_type)]

    sample['type'] = selected_type
    max_key = wine_df['key'].astype(int).max()
    sample['key'] = int(max_key) + 1

    for feature in quality_type_df.columns:
        if feature not in ['quality', 'type', 'key']:
            mean_value = quality_type_df[feature].mean()
            std_dev = quality_type_df[feature].std() * deviation_factor
            sample[feature] = round(np.random.uniform(mean_value - std_dev, mean_value + std_dev), 4)

    sample['quality'] = quality_score

    return pd.DataFrame.from_records([sample])

# Example usage
synthetic_sample = generate_sample_for_quality(wine_df)
print(synthetic_sample)

def g():

    project = hopsworks.login()
    fs = project.get_feature_store()

    new_wine = generate_sample_for_quality(wine_df)
    print(new_wine)

    wine_fg = fs.get_feature_group(name="wine_reduced_new",version=1)
    wine_fg.insert(new_wine)

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        stub.deploy("wine_daily")
        with stub.run():
            f()
