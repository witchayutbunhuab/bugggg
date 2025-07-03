from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Student

class Command(BaseCommand):
  help = 'สร้างข้อมูลนักเรียน (Student)'

  def add_arguments(self, parser):
    parser.add_argument('-n', '--number', type=int, default=10, help='จำนวนนักเรียนที่ต้องการสร้าง')

  def handle(self, *args, **options):
    num_students = options['number']
    fake = Faker('th_TH')

    for _ in range(num_students):
      student = Student(
        name=fake.name(),
        dob=fake.date_of_birth(minimum_age=18, maximum_age=30),
        email=fake.email()
      )
      student.save()

    self.stdout.write(self.style.SUCCESS(f'สร้างนักเรียน {num_students} คนเรียบร้อย'))
            