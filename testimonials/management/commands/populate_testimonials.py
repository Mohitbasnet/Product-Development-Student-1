from django.core.management.base import BaseCommand
from testimonials.models import Testimonial
from services.models import Service
class Command(BaseCommand):
    help = 'Populate testimonials with sample data linked to services'
    def handle(self, *args, **options):
        services = Service.objects.filter(is_active=True)[:5]
        if not services:
            self.stdout.write(
                self.style.ERROR('No active services found. Please create some services first.')
            )
            return
        testimonials_data = [
            {
                'customer_name': 'Samantha Lee',
                'company': 'Orion Tech',
                'job_title': 'Operations Manager',
                'service_slug': 'ai-powered-virtual-assistant',  
                'rating': 5,
                'content': 'DocuMind has completely changed how our teams handle documentation. Before, we wasted hours searching for information buried in long PDFs or emails. Now, with AI-driven summaries and instant answers, we save at least 30% of our time weekly. The compliance scanner also caught risks we would have easily missed. It feels like having a super-smart assistant that never forgets.',
                'is_featured': True,
                'is_approved': True,
            },
            {
                'customer_name': 'Rajesh Patel',
                'company': 'GreenWave Retail & Co.',
                'job_title': 'CFO',
                'service_slug': 'predictive-analytics-platform',  
                'rating': 5,
                'content': 'FinSight has given us unprecedented visibility into our company\'s finances. The predictive budgeting tool helped us forecast a seasonal dip months before it hit, saving us from overspending. The AI-driven fraud detection caught duplicate invoices that even our accountants overlooked. It\'s like having a CFO powered by AI working 24/7.',
                'is_featured': True,
                'is_approved': True,
            },
            {
                'customer_name': 'Michael Reed',
                'company': 'Vaux Brewery',
                'job_title': 'Supply Chain Manager',
                'service_slug': 'intelligent-process-automation',  
                'rating': 4,
                'content': 'Log AI has revolutionized our inventory management system. The AI-driven optimization has helped us maintain perfect stock levels, reducing both overstock and stockouts. The real-time tracking and predictive analytics have made our supply chain more efficient, and we\'re now able to make data-driven decisions that save both time and money. The seamless integration with our existing systems was a huge plus. Log AI is a must-have for any business looking to streamline inventory operations and stay ahead of the competition!',
                'is_featured': True,
                'is_approved': True,
            },
            {
                'customer_name': 'James Lee',
                'company': 'Samsung Electronics',
                'job_title': 'Regional Manager',
                'service_slug': 'computer-vision-solutions',  
                'rating': 5,
                'content': 'LaundriQ is a groundbreaking innovation that perfectly complements Samsung\'s commitment to smart home solutions. As a regional manager, I\'ve seen firsthand how this AI-powered tool enhances the laundry experience for our customers. By intelligently detecting fabric quality and optimizing detergent usage, LaundriQ not only ensures superior cleaning results but also supports eco-friendly practices. This collaboration with LaundriQ aligns with our vision of creating smarter, more sustainable home appliances. It\'s truly a game-changer in the world of laundry care.',
                'is_featured': False,
                'is_approved': True,
            },
            {
                'customer_name': 'Michael Grant',
                'company': 'Titan Manufacturing',
                'job_title': 'Plant Manager',
                'service_slug': 'digital-employee-experience-analytics',  
                'rating': 5,
                'content': 'SafeOps has been a game-changer for our manufacturing unit. The AI detects hazards in real-time and even predicts equipment failures that could have cost us millions. Compliance reporting that used to take days is now done in minutes. Our workplace has never been safer or more efficient.',
                'is_featured': False,
                'is_approved': True,
            },
        ]
        created_count = 0
        for data in testimonials_data:
            service_slug = data.pop('service_slug')
            try:
                service = Service.objects.get(slug=service_slug, is_active=True)
                self.stdout.write(f'Found service: {service.title} (slug: {service_slug})')
            except Service.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'Service with slug "{service_slug}" not found, skipping testimonial for {data["customer_name"]}')
                )
                continue
            data['service'] = service
            testimonial, created = Testimonial.objects.get_or_create(
                customer_name=data['customer_name'],
                company=data['company'],
                defaults=data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created testimonial for {data["customer_name"]} from {data["company"]} linked to {service.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Testimonial for {data["customer_name"]} from {data["company"]} already exists')
                )
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new testimonials')
        )