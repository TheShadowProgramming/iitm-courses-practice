# Pillow package and resizing images with different resolution according to our wish

- sometimes the user uploads a picture with a resolution which is not ideal for the pfp logo that we have 
- output_size = (125, 125) [here the numbers are width and height respectively]
- then we use the i = Image.open(picture_file)
- then we resize using the thumbnail method :- 
i.thumbnail(output_size)
i.save(picture_path)

# Displaying custom parts of datetime on the screen according to our wish

- use the method strftime('%Y-%m-%d'), this method will only display the year, month and the date of the datetime object jispe you're using the method
- we can look online for more tricks to check how to load the datetime object
