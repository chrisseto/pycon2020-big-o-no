import pytest
from app.models import Project

def pytest_generate_tests(metafunc):
    # NOTE: Primary key look ups will fail against CRDB
    # as they are not sequential values
    # (Project.objects.filter(id=549211255627808770), ('contributors__user__emails', )),
    # (Project.objects.filter(id=549211255629545474), ('contributors__user__emails', 'contributors__user')),
    # (Project.objects.filter(id=549211255629545474), ('tags', )),
    # (Project.objects.filter(id=549211255629545474), ('tags', 'contributors__user')),
    # (Project.objects.filter(id=549211255629545474), ('tags', 'contributors__user__emails')),
    metafunc.parametrize('queryset,includeargs', [
        (Project.objects.filter(id=50), ('contributors__user__emails', )),
        (Project.objects.filter(id=200), ('contributors__user__emails', 'contributors__user')),
        (Project.objects.filter(id=75), ('tags', )),
        (Project.objects.filter(id=75), ('tags', 'contributors__user')),
        (Project.objects.filter(id=75), ('tags', 'contributors__user__emails')),
        (Project.objects.all()[:25], ('tags', 'contributors__user__emails')),
        (Project.objects.filter(title__startswith='S')[:5], ('tags', 'contributors__user__emails')),
    ], ids=[
        'pk_load',
        'pk_load1',
        'tags',
        'tags_contributors_user',
        'tags_contributors_user_emails',
        'tags_contributors_user_emails_25',
        'tags_contributors_user_emails_filter_5',
    ])

def bench_include(queryset, includeargs):
    return list(queryset.include(*includeargs))

def bench_prefetch_related(queryset, includeargs):
    return list(queryset.prefetch_related(*includeargs))

@pytest.mark.django_db
def test_bench_include(benchmark, queryset, includeargs):
    assert len(benchmark(bench_include, queryset, includeargs)) != 0

@pytest.mark.django_db
def test_bench_prefetch_related(benchmark, queryset, includeargs):
    assert len(benchmark(bench_prefetch_related, queryset, includeargs)) != 0
