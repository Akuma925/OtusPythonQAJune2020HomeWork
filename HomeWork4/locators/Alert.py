class Alert:
    SUCCESS_ALERT = {'css': '.alert-success'}
    SUCCESS_ALERT_LOGIN = 'login'
    DANGER_ALERT = {'css': '.alert-danger'}
    SUCCESS_ALERT_TO_CART = {'css': SUCCESS_ALERT['css'] + ' > a:nth-child(2)'}
    SUCCESS_ALERT_TO_WISH_LIST = 'wish list'
