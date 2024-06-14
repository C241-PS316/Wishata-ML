# ML-Wishata-Capstone
## Overview
This is a capstone project focused on classifying tourist destination images into three different categories based on Scenery, Environmet and category.

## Scenery, Environment, Category
**Scenery** consist of **Nature** and **Urban**. It refers to visually stunning destinations that encompass both natural and urban environments. This includes a variety of landscapes, whether it’s the vibrant cityscapes of urban areas or the tranquil and untouched natural settings.

**Environment** covers the **Water** and the **Land**. Highlighting destinations with both water and land features. Land environments consist of lush forests, majestic mountains, a bunch of interesting places. Water environments include breathtaking oceans, serene rivers, picturesque lakes. 

**Category** consist of **Attractions**, **Historical**, and **Greenery**.  Attractions have unique features and  entertainment value, such as amusement parks, iconic landmarks, zoo, and waterboom. Historical sites are locations of significant historical importance, preserved for their cultural heritage. These include ancient ruins, grand monuments, and museums. Greenery includes destinations rich in plant life and natural beauty, such as serene parks, gardens, and forests.

## Datasets 
This project consist of 900 images for each class. With the total of the datasets consist of 6300 images.

**Scenery**: 
- **Nature** : 900 images
- **Urban** : 900 images

**Environment**:
- **Land** : 900 images
- **Water** : 900 images

**Categorical**:
- **Attractions** : 900 images
- **Historical** : 900 images
- **Greenery** : 900 images

## How to Use
1. Clone the repository.
2. Create Conda environment 
```conda create env -f env.yml```
3. Activate the Conda environment 
```conda activate wishata```
4. Run the notebook:
open and run the `wishata_TFLite.ipynb` notebook

## Additional Information
1. `convert.py` - This script converts the model from .h5 format to .tflite format.
2. `test.py` - This script tests the performance of the model using the test dataset.
3. `dispatcher_v2.py` - This script sorts and labels the dataset files appropriately.




