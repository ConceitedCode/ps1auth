from django.conf.urls import patterns, include, url
from billing import get_integration
pay_pal = get_integration("pay_pal")

urlpatterns = patterns('',
# moved to top level
# ( r'^paypal-ipn-handler/', include(pay_pal.urls) ),
)
