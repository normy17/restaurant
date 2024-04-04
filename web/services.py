def filter_rest(rests_qs, filters):
    if 'choice' in filters:
        rests_qs = rests_qs.filter(specialization__name__exact=filters['choice'])

    return rests_qs