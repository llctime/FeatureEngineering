# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import pandas as pd

    # 数据加载
    train = pd.read_csv('D:\\Dev\\Data\\train.csv')

    # 查看各个字段 唯一值个数
    for feature in train.columns:
        print('{}特征 唯一值个数{}'.format(feature, train[feature].nunique()))
        # 判断唯一值个数是否为1
        if train[feature].nunique() == 1:
            print(feature, ' 唯一值为1 ##################################')

    # sns.countplot()函数，以bar的形式展示每个类别的数量
    import seaborn as sns

    import matplotlib.pyplot as plt

    plt.figure(figsize=(20, 8))

    # 从直方图中可以看到 E,F,G更容易违约
    sns.countplot(x='grade', hue='isDefault', data=train)
    #plt.show()

    # float64, int64, object
    train.info()
    # 找到dtypes为float，设置为 数值类型特征
    num_features = train.select_dtypes(include=float).columns
    print(num_features)

    # 找到dtypes不为float，设置为 分类类型特征
    cat_features = train.select_dtypes(exclude=float).columns
    print(cat_features)

    # 查看缺失值
    temp = train.isnull().sum()
    print(temp[temp > 0])
    # 分类特征，进行缺失值补全，方法待定
    print(train[cat_features].isnull().sum())
    # 数值特征，采用中位数进行补全
    temp = train[num_features].isnull().sum()
    temp = temp[temp > 0]
    for f in temp.index:
        print(f, train[f].median())
        train[f].fillna(train[f].median(), inplace=True)
    train[num_features].isnull().sum()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
