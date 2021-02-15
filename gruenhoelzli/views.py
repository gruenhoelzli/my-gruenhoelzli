from juntagrico.view_decorators import create_subscription_session
from juntagrico.views_create_subscription import CSSummaryView

# Skip share and abo steps in sign-up
@create_subscription_session
def cs_select_subscription(request, cs_session):
    return CSSummaryView.post(request, cs_session)
