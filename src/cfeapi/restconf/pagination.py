from rest_framework import pagination



class CFEAPIPagination(pagination.LimitOffsetPagination): #PageNumberPagination):
    #page_size   =  20
    default_limit   = 10
    max_limit       = 20
    #limit_query_param = 'lim' 
