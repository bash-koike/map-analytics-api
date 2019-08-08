
# ------------------------------------
# Build zip file to upload to Lambda
# ------------------------------------

# If error occured at run `pip install ..`, create `~/.pydistutils.cfg` file
# and put the following text.
#
# [install]
# prefix=

rm upload.zip

cd app
zip -r ../upload.zip api handlers libs -x '*__pycache__*'
cd ..

pip install --target ./package requests
cd package
zip -r ../upload.zip *
cd ..
rm -rf package
