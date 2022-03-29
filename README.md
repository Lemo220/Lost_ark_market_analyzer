# Lost_ark_market_analyzer

Bot analyze market in-game. Monitor most important categories (enchant materials, trade goods). It crop main screen, analyze values/text on cropped image and transform it. After that, send data to local database to later analyse everything.


How looks regular screen from market:

![screen_of_market](https://user-images.githubusercontent.com/87129963/160636777-a162649d-9c05-4f82-b145-3d23881eb1cb.PNG)


Cropped image with grayscale:

![image_grayscale](https://user-images.githubusercontent.com/87129963/160633526-ebe5f9af-4bdb-4d15-bd6b-808db982fe1d.png)


Apply filter2D with kernel to get sharper image (without transforms, pytesseract has problems to read text on image)

![after_filter2D](https://user-images.githubusercontent.com/87129963/160633872-c4520dc3-724a-478c-afa8-25efb7d3ee89.png)

After all, just resized image to get better result.
Had to use also config to pytesseract with oem 0 - best results with that one.

To numbers have to use more transformations, pytesseract has problem to read exact value with high repeatability, now it has around 98-99% correct answers. I used also dilate and threshold to get clear picture. 
Pytesseract with oem 3 and psm 7 has best results.
