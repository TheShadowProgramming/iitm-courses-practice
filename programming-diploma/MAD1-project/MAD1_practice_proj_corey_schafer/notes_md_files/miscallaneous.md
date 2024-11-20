# Pillow package and resizing images with different resolution according to our wish

- sometimes the user uploads a picture with a resolution which is not ideal for the pfp logo that we have 
- output_size = (125, 125) [here the numbers are width and height respectively]
- then we use the i = Image.open(picture_file)
- then we resize using the thumbnail method :- 
i.thumbnail(output_size)
i.save(picture_path)