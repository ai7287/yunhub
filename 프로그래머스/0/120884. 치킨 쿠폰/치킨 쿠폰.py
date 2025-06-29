def solution(chicken):
    service = 0
    coupon = chicken
    
    while coupon >= 10:
        new_service = coupon // 10
        service += new_service
        coupon = coupon % 10 + new_service
        
    return service
