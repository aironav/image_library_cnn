if __name__ == "__main__":
    path = 'mytensorflow/Dataset/training_set'                  # path of the image dataset
    a = MasterImage(PATH=path,
                    IMAGE_SIZE=80)

    X_Data,Y_Data = a.load_dataset()
    print(X_Data.shape)
