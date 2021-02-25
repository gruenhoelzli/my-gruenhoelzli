from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.loader import get_template
from juntagrico.dao.activityareadao import ActivityAreaDao
from juntagrico.dao.jobdao import JobDao

from juntagrico.view_decorators import create_subscription_session
from juntagrico.views_create_subscription import CSSummaryView
from juntagrico.views import get_menu_dict

# Skip share and abo steps in sign-up
@create_subscription_session
def cs_select_subscription(request, cs_session):
    return CSSummaryView.post(request, cs_session)

# Make sure no invalid messages like 'messages/no_subscription.html' appear on home screen
def home_messages_without_subscription_and_shares(request):
    result = []
    member = request.user.member
    if member.confirmed is False:
        result.append(get_template('messages/not_confirmed.html').render())
    return result

# I didn't find a better way to customize the home screen messages than to copy this code from juntagrico.views.home
@login_required
def home(request):
    '''
    Overview on juntagrico
    '''

    next_jobs = set(JobDao.get_current_jobs()[:7])
    pinned_jobs = set(JobDao.get_pinned_jobs())
    next_promotedjobs = set(JobDao.get_promoted_jobs())
    renderdict = get_menu_dict(request)
    renderdict['messages'].extend(home_messages_without_subscription_and_shares(request))
    renderdict.update({
        'jobs': sorted(next_jobs.union(pinned_jobs).union(next_promotedjobs), key=lambda job: job.time),
        'areas': ActivityAreaDao.all_visible_areas_ordered(),
    })

    return render(request, 'home.html', renderdict)
