class ProductPage:
    PRODUCT_PAGE_URL = f'/index.php?route=product/product&path=57&product_id='
    ADD_TO_WISHLIST = {'css': '[data-original-title="Add to Wish List"]'}
    ADD_TO_CART = {'css': '#button-cart'}
    PRODUCT_NAME = {'css': '#content .col-sm-4 h1'}
    PRODUCT_PRICE = {'css': 'content .row .col-sm-4 h2'}
    CLICK_REVIEW = {'css': '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li.active > a'}
    SEND_REVIEW = {'css': '.pull-right #button-review'}
