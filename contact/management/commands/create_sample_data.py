from django.core.management.base import BaseCommand
from django.utils import timezone
from contact.models import ContactInquiry
from gallery.models import Photo
from events.models import Event
from news.models import Article
from testimonials.models import Testimonial
from services.models import Service
import json

class Command(BaseCommand):
    help = 'Create sample data for testing the AI-Solutions website'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample contact inquiries
        contact_inquiries = [
            {
                'name': 'John Smith',
                'email': 'john.smith@techcorp.com',
                'phone': '+44 20 7123 4567',
                'company': 'TechCorp Ltd',
                'country': 'United Kingdom',
                'job_title': 'CTO',
                'job_details': 'We need AI solutions for automating our customer service processes and improving data analytics capabilities.',
                'is_processed': False
            },
            {
                'name': 'Sarah Johnson',
                'email': 'sarah.j@innovate.com',
                'phone': '+1 555 123 4567',
                'company': 'Innovate Solutions',
                'country': 'United States',
                'job_title': 'Product Manager',
                'job_details': 'Looking for AI-powered prototyping solutions to accelerate our product development cycle.',
                'is_processed': True,
                'notes': 'Follow up scheduled for next week'
            },
            {
                'name': 'Michael Chen',
                'email': 'm.chen@globaltech.com',
                'phone': '+86 138 0013 8000',
                'company': 'Global Tech',
                'country': 'China',
                'job_title': 'Head of Engineering',
                'job_details': 'Interested in AI solutions for digital employee experience enhancement and workflow optimization.',
                'is_processed': False
            }
        ]
        
        for inquiry_data in contact_inquiries:
            ContactInquiry.objects.get_or_create(
                email=inquiry_data['email'],
                defaults=inquiry_data
            )
        
        # Create sample services
        services = [
            {
                'title': 'AI-Powered Virtual Assistant',
                'slug': 'ai-virtual-assistant',
                'short_description': 'Intelligent virtual assistant that responds to user inquiries and provides AI-based solutions.',
                'description': 'Our AI-powered virtual assistant leverages cutting-edge natural language processing to provide intelligent responses to user inquiries. It offers 24/7 support and can handle complex queries with high accuracy.',
                'icon': 'fas fa-robot',
                'category': 'ai_solutions',
                'features': json.dumps([
                    'Natural Language Processing',
                    '24/7 Availability',
                    'Multi-language Support',
                    'Learning Capabilities',
                    'Integration Ready'
                ]),
                'is_featured': True,
                'is_active': True,
                'price_starting_from': 299.99
            },
            {
                'title': 'Rapid Prototyping Solutions',
                'slug': 'rapid-prototyping',
                'short_description': 'AI-based affordable prototyping solutions to speed up design and engineering processes.',
                'description': 'Accelerate your design and engineering workflows with our AI-powered prototyping solutions. Generate prototypes quickly and cost-effectively while maintaining high quality standards.',
                'icon': 'fas fa-cogs',
                'category': 'automation',
                'features': json.dumps([
                    'Fast Prototype Generation',
                    'Cost-Effective Solutions',
                    'Quality Assurance',
                    'Customizable Templates',
                    'Team Collaboration'
                ]),
                'is_featured': True,
                'is_active': True,
                'price_starting_from': 199.99
            },
            {
                'title': 'Digital Employee Experience Analytics',
                'slug': 'employee-experience-analytics',
                'short_description': 'Comprehensive analytics platform for monitoring and improving digital employee experience.',
                'description': 'Monitor and analyze digital employee experience metrics to identify issues and opportunities for improvement. Get actionable insights to enhance productivity and satisfaction.',
                'icon': 'fas fa-chart-line',
                'category': 'data_analytics',
                'features': json.dumps([
                    'Real-time Monitoring',
                    'Predictive Analytics',
                    'Custom Dashboards',
                    'Automated Reporting',
                    'Performance Insights'
                ]),
                'is_featured': False,
                'is_active': True,
                'price_starting_from': 399.99
            }
        ]
        
        for service_data in services:
            Service.objects.get_or_create(
                slug=service_data['slug'],
                defaults=service_data
            )
        
        # Create sample testimonials
        testimonials = [
            {
                'customer_name': 'David Wilson',
                'company': 'FutureTech Industries',
                'job_title': 'CEO',
                'rating': 5,
                'content': 'AI-Solutions transformed our digital workplace. Their AI-powered virtual assistant has improved our customer service efficiency by 300%. Highly recommended!',
                'is_featured': True,
                'is_approved': True
            },
            {
                'customer_name': 'Emma Thompson',
                'company': 'InnovateLab',
                'job_title': 'Head of Product',
                'rating': 5,
                'content': 'The rapid prototyping solutions saved us months of development time. The quality is outstanding and the team is incredibly professional.',
                'is_featured': True,
                'is_approved': True
            },
            {
                'customer_name': 'James Rodriguez',
                'company': 'TechForward',
                'job_title': 'CTO',
                'rating': 4,
                'content': 'Great AI solutions with excellent support. The analytics platform helped us identify key areas for improvement in our digital processes.',
                'is_featured': False,
                'is_approved': True
            }
        ]
        
        for testimonial_data in testimonials:
            Testimonial.objects.get_or_create(
                customer_name=testimonial_data['customer_name'],
                company=testimonial_data['company'],
                defaults=testimonial_data
            )
        
        # Create sample articles
        articles = [
            {
                'title': 'The Future of AI in Digital Employee Experience',
                'slug': 'future-ai-digital-employee-experience',
                'content': 'Artificial Intelligence is revolutionizing how employees interact with digital systems. This comprehensive guide explores the latest trends and technologies shaping the future of workplace digitalization.',
                'excerpt': 'Explore how AI is transforming digital employee experience and what it means for the future of work.',
                'author': 'Dr. Sarah Mitchell',
                'category': 'ai_news',
                'is_published': True,
                'is_featured': True,
                'tags': 'AI, Digital Experience, Future of Work, Technology',
                'published_date': timezone.now()
            },
            {
                'title': 'AI-Solutions Wins Innovation Award 2024',
                'slug': 'ai-solutions-wins-innovation-award-2024',
                'content': 'We are thrilled to announce that AI-Solutions has been awarded the prestigious Innovation Award 2024 for our groundbreaking work in AI-powered digital employee experience solutions.',
                'excerpt': 'AI-Solutions recognized for innovation in AI-powered digital workplace solutions.',
                'author': 'Marketing Team',
                'category': 'company_news',
                'is_published': True,
                'is_featured': True,
                'tags': 'Award, Innovation, Recognition, Company News',
                'published_date': timezone.now()
            }
        ]
        
        for article_data in articles:
            Article.objects.get_or_create(
                slug=article_data['slug'],
                defaults=article_data
            )
        
        # Create sample events
        events = [
            {
                'title': 'AI Innovation Summit 2024',
                'description': 'Join us for the premier AI Innovation Summit featuring industry leaders, cutting-edge demonstrations, and networking opportunities.',
                'date': timezone.now() + timezone.timedelta(days=30),
                'location': 'Sunderland Convention Centre',
                'event_type': 'upcoming',
                'is_featured': True,
                'registration_url': 'https://example.com/register',
                'max_attendees': 500,
                'current_attendees': 150
            },
            {
                'title': 'Digital Transformation Workshop',
                'description': 'Hands-on workshop covering the latest digital transformation strategies and AI implementation best practices.',
                'date': timezone.now() - timezone.timedelta(days=15),
                'location': 'Online',
                'event_type': 'past',
                'is_featured': False,
                'max_attendees': 100,
                'current_attendees': 95
            }
        ]
        
        for event_data in events:
            Event.objects.get_or_create(
                title=event_data['title'],
                date=event_data['date'],
                defaults=event_data
            )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write('Sample data includes:')
        self.stdout.write('- 3 Contact Inquiries')
        self.stdout.write('- 3 Services')
        self.stdout.write('- 3 Testimonials')
        self.stdout.write('- 2 Articles')
        self.stdout.write('- 2 Events')
