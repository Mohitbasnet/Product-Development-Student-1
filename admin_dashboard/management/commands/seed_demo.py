from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from faker import Faker
import random

from contact.models import ContactInquiry
from news.models import Article
from events.models import Event
from testimonials.models import Testimonial
from services.models import Service
from gallery.models import Photo


class Command(BaseCommand):
    help = "Seed demo data across apps (images optional)."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=10, help="Count per model where applicable")

    def handle(self, *args, **options):
        fake = Faker()
        count = options["count"]
        now = timezone.now()

        # Services
        categories = [c for c, _ in Service.CATEGORY_CHOICES]
        icons = [
            "fas fa-robot", "fas fa-cogs", "fas fa-chart-line", "fas fa-brain",
            "fas fa-database", "fas fa-gears", "fas fa-bolt"
        ]
        for i in range(count):
            title = f"Service {fake.word().title()} {i+1}"
            slug = f"service-{i+1}-{fake.word()}"
            svc, _ = Service.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title,
                    "description": fake.paragraph(nb_sentences=5),
                    "short_description": fake.sentence(nb_words=10),
                    "icon": random.choice(icons),
                    "category": random.choice(categories),
                    "features": '["Fast setup","Scalable","Secure"]',
                    "is_featured": random.choice([True, False]),
                    "is_active": True,
                    "price_starting_from": random.choice([None, 499, 999, 1499]) or None,
                }
            )

        # Articles
        article_categories = [c for c, _ in Article.CATEGORY_CHOICES]
        for i in range(count):
            title = f"{fake.catch_phrase()}"
            slug = f"article-{i+1}-{fake.word()}"
            Article.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title,
                    "content": "\n\n".join(fake.paragraphs(nb=8)),
                    "excerpt": fake.sentence(nb_words=20),
                    "author": fake.name(),
                    "category": random.choice(article_categories),
                    "is_published": random.choice([True, False, True]),
                    "is_featured": random.choice([True, False]),
                    "published_date": now - timedelta(days=random.randint(0, 120)),
                    "tags": ", ".join(fake.words(nb=5)),
                }
            )

        # Events
        for i in range(count):
            dt = now + timedelta(days=random.randint(-60, 60))
            etype = "upcoming" if dt > now else "past"
            Event.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=6),
                date=dt,
                location=fake.city(),
                event_type=etype,
                is_featured=random.choice([True, False]),
                registration_url=fake.url(),
                max_attendees=random.choice([None, 50, 100, 200]),
                current_attendees=random.randint(0, 50),
            )

        # Testimonials
        for i in range(count):
            Testimonial.objects.create(
                customer_name=fake.name(),
                company=fake.company(),
                job_title=fake.job(),
                rating=random.randint(4, 5),
                content=fake.paragraph(nb_sentences=5),
                is_featured=random.choice([True, False]),
                is_approved=random.choice([True, True, False]),
            )

        # Gallery Photos (no image required)
        photo_categories = [c for c, _ in Photo.CATEGORY_CHOICES]
        for i in range(count):
            Photo.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.sentence(nb_words=12),
                category=random.choice(photo_categories),
                is_featured=random.choice([True, False]),
            )

        # Contact Inquiries
        for i in range(count):
            ContactInquiry.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                company=fake.company(),
                country=fake.country(),
                job_title=fake.job(),
                job_details=fake.paragraph(nb_sentences=6),
                is_processed=random.choice([True, False]),
                notes=fake.sentence(),
            )

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))
