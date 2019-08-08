from libs import s3


def test_upload_file():
    res = s3.upload_file('bar.csv', 'foo/bar.csv')
    print(res)
    return res


if __name__ == "__main__":
    test_upload_file()
