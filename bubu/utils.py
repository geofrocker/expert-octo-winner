try:
    # >= 1.4
    from django.templatetags.static import static
    return static(path)
except ImportError:
    pass