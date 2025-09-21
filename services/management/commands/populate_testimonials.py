from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from testimonials.models import Testimonial
from services.models import Service


class Command(BaseCommand):
    help = 'Populate testimonials with sample data'

    def handle(self, *args, **options):
        # Get services for linking testimonials
        try:
            documind_service = Service.objects.get(slug='documind')
        except Service.DoesNotExist:
            documind_service = None
            
        try:
            finsight_service = Service.objects.get(slug='finsight')
        except Service.DoesNotExist:
            finsight_service = None
            
        try:
            log_ai_service = Service.objects.get(slug='log-ai')
        except Service.DoesNotExist:
            log_ai_service = None
            
        try:
            laundriq_service = Service.objects.get(slug='laundriq')
        except Service.DoesNotExist:
            laundriq_service = None
            
        try:
            safeops_service = Service.objects.get(slug='safeops')
        except Service.DoesNotExist:
            safeops_service = None

        # Sample testimonials data
        testimonials_data = [
            {
                'customer_name': 'Samantha Lee',
                'company': 'Orion Tech',
                'job_title': 'Operations Manager',
                'rating': 5,  # 4.7 rounded to 5
                'content': 'DocuMind has completely changed how our teams handle documentation. Before, we wasted hours searching for information buried in long PDFs or emails. Now, with AI-driven summaries and instant answers, we save at least 30% of our time weekly. The compliance scanner also caught risks we would have easily missed. It feels like having a super-smart assistant that never forgets.',
                'service': documind_service,
                'is_featured': True,
                'is_approved': True
            },
            {
                'customer_name': 'Rajesh Patel',
                'company': 'GreenWave Retail & Co.',
                'job_title': 'CFO',
                'rating': 5,  # 4.9 rounded to 5
                'content': 'FinSight has given us unprecedented visibility into our company\'s finances. The predictive budgeting tool helped us forecast a seasonal dip months before it hit, saving us from overspending. The AI-driven fraud detection caught duplicate invoices that even our accountants overlooked. It\'s like having a CFO powered by AI working 24/7.',
                'service': finsight_service,
                'is_featured': True,
                'is_approved': True
            },
            {
                'customer_name': 'Michael Reed',
                'company': 'Vaux Brewery',
                'job_title': 'Supply Chain Manager',
                'rating': 4,  # 4.4 rounded to 4
                'content': 'Log AI has revolutionized our inventory management system. The AI-driven optimization has helped us maintain perfect stock levels, reducing both overstock and stockouts. The real-time tracking and predictive analytics have made our supply chain more efficient, and we\'re now able to make data-driven decisions that save both time and money. The seamless integration with our existing systems was a huge plus. Log AI is a must-have for any business looking to streamline inventory operations and stay ahead of the competition!',
                'service': log_ai_service,
                'is_featured': True,
                'is_approved': True
            },
            {
                'customer_name': 'James Lee',
                'company': 'Samsung Electronics',
                'job_title': 'Regional Manager',
                'rating': 5,  # 4.7 rounded to 5
                'content': 'LaundriQ is a groundbreaking innovation that perfectly complements Samsung\'s commitment to smart home solutions. As a regional manager, I\'ve seen firsthand how this AI-powered tool enhances the laundry experience for our customers. By intelligently detecting fabric quality and optimizing detergent usage, LaundriQ not only ensures superior cleaning results but also supports eco-friendly practices. This collaboration with LaundriQ aligns with our vision of creating smarter, more sustainable home appliances. It\'s truly a game-changer in the world of laundry care.',
                'service': laundriq_service,
                'is_featured': False,
                'is_approved': True
            },
            {
                'customer_name': 'Michael Grant',
                'company': 'Titan Manufacturing',
                'job_title': 'Plant Manager',
                'rating': 5,  # 4.7 rounded to 5
                'content': 'SafeOps has been a game-changer for our manufacturing unit. The AI detects hazards in real-time and even predicts equipment failures that could have cost us millions. Compliance reporting that used to take days is now done in minutes. Our workplace has never been safer or more efficient.',
                'service': safeops_service,
                'is_featured': False,
                'is_approved': True
            }
        ]

        # Create testimonials
        for testimonial_data in testimonials_data:
            testimonial = Testimonial.objects.create(**testimonial_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created testimonial: {testimonial.customer_name} - {testimonial.company}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated {len(testimonials_data)} testimonials')
        )
