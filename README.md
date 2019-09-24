# amazon-product-review-analysis
It pulls the reviews on amazon for a particular product and do the analysis that if it's original or fake on the basis of reviews.

Step 1: Install scrapy in your system pip install scrapy

Step 2: Create a scrapy project scrapy startproject amazonreviews

Step 3: After te creation of project, go to the inner folder amazonreviews cd amazonreviews/amazonreviews

Step 4: Now create a spider to crawl on the site. This will create a folder called spider in your directory. scrapy genspider amazon_review amazon.in

Step 5: Now run the script scrapping.py, this will create a csv file containing ratings,title and reviews cd spider scrapy runspider scrapping.py -o reviews.csv
