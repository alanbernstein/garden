import random
from django.core.management.base import BaseCommand, CommandError
from issues.models import User, Issue


garden_polygon = [
    [-76.9492051, 38.8763236],
    [-76.9494841, 38.8771276],
    [-76.9498864, 38.8772153],
    [-76.9501385, 38.8771568],
    [-76.9502726, 38.8770378],
    [-76.9503531, 38.8768582],
    [-76.9507125, 38.8765951],
    [-76.9506937, 38.8763445],
    [-76.9502914, 38.8761566],
    [-76.9498783, 38.8761232],
    [-76.9492051, 38.8763236],
]


def in_polygon(xq, yq, poly):
    # test whether (xq, yq) is inside poly
    # https://stackoverflow.com/questions/217578/how-can-i-determine-whether-a-2d-point-is-within-a-polygon/2922778#2922778
    x, y = zip(*poly)

    i, j, c = 0, len(x)-1, False
    while i < len(x):
        if ((y[i] > yq) != (y[j] > yq) and
            (xq < (x[j]-x[i]) * (yq-y[i]) / (y[j]-y[i]) + x[i])):
            c = not c

        i, j = i+1, i

    return c


def random_lonlat_poly(poly):
    x, y = zip(*poly)
    xmin, xmax, ymin, ymax = min(x), max(x), min(y), max(y)

    while True:
        # bad idea for general polygon, but fine here
        lon = random.random() * (xmax-xmin) + xmin
        lat = random.random() * (ymax-ymin) + ymin
        if in_polygon(lon, lat, poly):
            return lon, lat


class Command(BaseCommand):
    help = 'generate some fake data and insert into database'

    def add_arguments(self, parser):
        parser.add_argument('nuke_db', default=False, type=bool)
        parser.add_argument('num_issues', default=10, type=int)
        parser.add_argument('issues_per_user', default=2, type=float)

    def handle(self, *args, **options):
        if options['nuke_db']:
            User.objects.all().delete()
            Issue.objects.all().delete()

        num_users = options['num_issues'] / options['issues_per_user']

        for n in range(num_users):
            User.objects.create(name='pubert')

        all_users = User.objects.all()
        for n in range(options['num_issues']):
            lon, lat = random_lonlat_poly(garden_polygon)
            Issue.objects.create(
                title='foo',
                details='bar',
                user=random.choice(all_users),
                lon=lon,
                lat=lat,
            )

        self.stdout.write(self.style.SUCCESS('generated %d fake issues' % options['num_issues']))
