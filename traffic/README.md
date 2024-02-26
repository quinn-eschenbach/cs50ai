# MY FIRST NEURAL NETWORKs:

📼 Youtube link: https://youtu.be/R4vyS-pyiUE

## 1. Step
For the first neural network i copy pasted the code from the lecture nodes and changed it to use the new image resolution.
The layers were like this:
- Conv2D (32, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (128, "relu")
- Dropout(0.5)
- Dense(NUM_CATEGORIES)

I dont think it will work very well since it was used for the handwriting and is not optimized for this task. This run is just to get familiar with the tesorflow library

**RESULT**: `333/333 - 2s - loss: 0.1175 - accuracy: 0.0544 - 2s/epoch - 7ms/step`

As expected the results were pretty bad, only 5% accuracy. But the import and training is working from here we can start to improve this bad boy.

## 2. Step
Next I'll try to add more nodes to the Dense layer, it should already improve our model since the 128 from before are way to little for 30x30 images with three color layers.
The layers are like this:
- Conv2D (32, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (3000, "relu")
- Dropout(0.5)
- Dense(NUM_CATEGORIES)

**RESULT** `333/333 - 17s - loss: 0.0179 - accuracy: 0.9352 - 17s/epoch - 50ms/step`

Just increasing the Dense layer size increases the the accuracy A LOT but results in much longer training times (17s/epoch). For the next runs i will switch to my other laptop with more powerful hardware () 

## 3. Step 
I decided to try using two hidden dense layers. I started with two 128 layers
The layers are like this:
- Conv2D (32, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (128, "relu")
- Dropout(0.5)
- Dense (128, "relu")
- Dropout(0.5)
- Dense(NUM_CATEGORIES)

**RESULT** `333/333 - 1s - loss: 0.1043 - accuracy: 0.0524 - 961ms/epoch - 3ms/step`

Thats pretty much as bad as the first time, lets bump up these nodes

## 4. Step
The layers are like this:
- Conv2D (32, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (2048, "relu")
- Dropout(0.5)
- Dense (2048, "relu")
- Dropout(0.5)
- Dense(NUM_CATEGORIES)

**RESULT** `333/333 - 4s - loss: 0.0093 - accuracy: 0.9491 - 4s/epoch - 11ms/step`

We were able to get 1% more accuracy compared to step 2.

## 5. Step
Lets add a even bigger laye inbetween the two existing ones
- Conv2D (32, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (2048, "relu")
- Dropout(0.5)
- Dense (3072, "relu")
- Dropout(0.5)
- Dense (2048, "relu")
- Dropout(0.5)
- Dense(NUM_CATEGORIES)

**RESULT** `333/333 - 5s - loss: 0.0114 - accuracy: 0.9252 - 5s/epoch - 14ms/step`

that actually reduced the accuracy 

## 6. Step
Let stick with two but increase the node count again

- Conv2D (32, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (3072, "relu")
- Dropout(0.5)
- Dense (3072, "relu")
- Dropout(0.5)
- Dense(NUM_CATEGORIES)

**RESULT** ``33/333 - 6s - loss: 0.0122 - accuracy: 0.9300 - 6s/epoch - 17ms/step`

Thats worse then the 4. step, so lets stick with 2048 and reduce the dropout

## 7. Step
The layers are like this:
- Conv2D (32, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (2048, "relu")
- Dropout(0.3)
- Dense (2048, "relu")
- Dropout(0.3)
- Dense(NUM_CATEGORIES)

**RESULT** `333/333 - 3s - loss: 0.0095 - accuracy: 0.9545 - 3s/epoch - 10ms/step`

~95% thats great 🥳

## 8. Step
Let increase the matrix of our convolution step

The layers are like this:
- Conv2D (32, (5, 5), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (2048, "relu")
- Dropout(0.3)
- Dense (2048, "relu")
- Dropout(0.3)
- Dense(NUM_CATEGORIES)

**RESULT** `333/333 - 4s - loss: 0.0108 - accuracy: 0.9532 - 4s/epoch - 11ms/step`

Still ~95% 

## 9. Step
I decided to run the convultion step twice
The layers are like this:
- Conv2D (32, (5, 5), activation="relu")
- MaxPooling2D (2, 2)
- Conv2D (16, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (2048, "relu")
- Dropout(0.3)
- Dense (2048, "relu")
- Dropout(0.3)
- Dense(NUM_CATEGORIES)

**RESULT** `333/333 - 3s - loss: 0.0085 - accuracy: 0.9529 - 3s/epoch - 8ms/step`

That was a great idea, we still had the same performance but the training was way faster

## 10. Step
I increased the filters for the second conv2d layer
The layers are like this:
- Conv2D (32, (5, 5), activation="relu")
- MaxPooling2D (2, 2)
- Conv2D (16, (3, 3), activation="relu")
- MaxPooling2D (2, 2)
- Flatten()
- Dense (2048, "relu")
- Dropout(0.3)
- Dense (2048, "relu")
- Dropout(0.3)
- Dense(NUM_CATEGORIES)

**RESULT** `333/333 - 3s - loss: 0.0069 - accuracy: 0.9684 - 3s/epoch - 9ms/step`

I got over 96% accuracy! I think i will leave it here since im quite happy with the results