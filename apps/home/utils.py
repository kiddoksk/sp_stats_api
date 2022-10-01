from decimal import Decimal

from django.db.models import Avg, Sum


def get_average_value(queryset, term):
    """
    Get average of the given DB column from queryset
    """
    key = '{0}__avg'.format(term)
    return queryset.aggregate(Avg(term))[key]


def get_median_value(queryset, term):
    """
    Get average of the given DB column from queryset
    """
    count = queryset.count()
    values = queryset.values_list(term, flat=True).order_by(term)
    if count % 2 == 1:
        return values[int(round(count/2))]
    else:
        return sum(values[count/2-1:count/2+1])/Decimal(2.0)


def get_sum_value(queryset, term):
    """
    Get average of the given DB column from queryset
    """
    key = '{0}__sum'.format(term)
    return queryset.aggregate(Sum(term))[key]
