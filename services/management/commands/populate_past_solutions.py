from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from services.models import PastSolution
class Command(BaseCommand):
    help = 'Populate past solutions with sample data'
    def handle(self, *args, **options):
        PastSolution.objects.all().delete()
        solutions_data = [
            {
                'title': 'DocuMind',
                'slug': 'documind',
                'description': 'DocuMind is an AI-driven enterprise documentation assistant that revolutionizes how organizations create, manage, and search knowledge. It ensures employees spend less time hunting for information and more time acting on it. The solution integrates seamlessly with existing enterprise systems and provides intelligent document processing capabilities that adapt to each organization\'s unique needs.',
                'short_description': 'AI-driven enterprise documentation assistant that revolutionizes how organizations create, manage, and search knowledge.',
                'category': 'ai_solutions',
                'features': [
                    'Uses AI to auto-summarize and categorize large documents into concise knowledge snippets',
                    'Natural language query search (ask questions, get instant answers from company docs)',
                    'Real-time document translation into multiple languages',
                    'AI-powered compliance scanner to detect policy, legal, or security risks in text',
                    'Integrates with Slack, Teams, and company intranet for seamless collaboration',
                    'Advanced document versioning and change tracking',
                    'Customizable knowledge base templates'
                ],
                'technologies_used': [
                    'Python', 'Django', 'OpenAI GPT-4', 'Elasticsearch', 'Redis', 'Docker', 'AWS', 'React', 'TypeScript'
                ],
                'client_name': 'TechCorp Solutions',
                'project_duration': '6 months',
                'completion_date': date(2024, 3, 15),
                'is_featured': True,
                'is_published': True
            },
            {
                'title': 'Log AI',
                'slug': 'log-ai',
                'description': 'An innovative inventory management solution powered by artificial intelligence, designed to streamline and optimize inventory operations for businesses of all sizes. With intelligent automation, real-time analytics, and predictive capabilities, Log AI transforms how organizations manage stock, supply chains, and operational logistics. The system provides comprehensive visibility into inventory levels and predicts future demand patterns.',
                'short_description': 'AI-powered inventory management solution that streamlines and optimizes inventory operations for businesses of all sizes.',
                'category': 'ai_solutions',
                'features': [
                    'Automatically adjusts inventory levels based on demand forecasting and sales trends',
                    'Tracks inventory across warehouses, stores, and delivery networks with precision',
                    'Leverages AI to forecast future demand patterns and seasonal trends',
                    'Seamlessly integrates with existing ERP, POS, and supply chain systems',
                    'Real-time alerts for low stock and overstock situations',
                    'Automated reorder point calculations',
                    'Multi-location inventory synchronization'
                ],
                'technologies_used': [
                    'Python', 'TensorFlow', 'PostgreSQL', 'FastAPI', 'Celery', 'Kubernetes', 'Vue.js', 'Chart.js'
                ],
                'client_name': 'RetailMax Inc.',
                'project_duration': '4 months',
                'completion_date': date(2024, 1, 20),
                'is_featured': True,
                'is_published': True
            },
            {
                'title': 'FinSight',
                'slug': 'finsight',
                'description': 'An AI-powered financial insights platform designed to help organizations track expenses, forecast budgets, and optimize financial planning. FinSight provides comprehensive financial analytics with intelligent automation that helps businesses make data-driven financial decisions. The platform offers real-time monitoring and predictive analytics for better financial control.',
                'short_description': 'AI-powered financial insights platform for expense tracking, budget forecasting, and financial planning optimization.',
                'category': 'fintech',
                'features': [
                    'AI-based anomaly detection for unusual spending or fraud risks',
                    'Predictive modeling for cash flow and revenue streams',
                    'Auto-categorization of expenses from receipts and invoices',
                    'Personalized budgeting recommendations for departments',
                    'Smart alerts for overspending, budget risks, or duplicate transactions',
                    'Advanced financial reporting and visualization',
                    'Integration with major accounting software'
                ],
                'technologies_used': [
                    'Python', 'Django', 'Pandas', 'Scikit-learn', 'PostgreSQL', 'Celery', 'React', 'D3.js', 'AWS'
                ],
                'client_name': 'FinanceFlow Ltd.',
                'project_duration': '5 months',
                'completion_date': date(2023, 11, 10),
                'is_featured': True,
                'is_published': True
            },
            {
                'title': 'LaundriQ',
                'slug': 'laundriq',
                'description': 'LaundriQ is a cutting-edge AI-powered solution designed to redefine laundry care by delivering unparalleled convenience, precision, and fabric protection. Developed in collaboration with Samsung washing machines, LaundriQ leverages advanced artificial intelligence to analyze fabric quality, optimize detergent usage, and select the ideal washing mode for every load. The system ensures optimal care for different fabric types while minimizing resource usage.',
                'short_description': 'AI-powered laundry care solution that optimizes washing modes and detergent usage for Samsung washing machines.',
                'category': 'iot',
                'features': [
                    'Uses AI to assess fabric type, condition, and quality in real-time',
                    'Ensures gentle yet effective care tailored to each garment',
                    'Precisely calculates the required detergent amount based on load size, fabric sensitivity, and soil level',
                    'Minimizes water and energy usage through smart load assessment and cycle adjustments',
                    'Connects with Samsung SmartThings for remote control and monitoring',
                    'Machine learning algorithms that improve over time',
                    'Mobile app for personalized laundry management'
                ],
                'technologies_used': [
                    'Python', 'TensorFlow', 'IoT Sensors', 'Samsung SmartThings API', 'React Native', 'MQTT', 'Docker'
                ],
                'client_name': 'Samsung Electronics',
                'project_duration': '8 months',
                'completion_date': date(2023, 8, 25),
                'is_featured': True,
                'is_published': True
            },
            {
                'title': 'SafeOps',
                'slug': 'safeops',
                'description': 'SafeOps is an AI-powered workplace safety and compliance monitoring solution for factories, warehouses, and offices. The system uses computer vision and machine learning to monitor workplace environments in real-time, detecting potential safety hazards and ensuring compliance with safety regulations. SafeOps helps organizations maintain a safe working environment while reducing accidents and improving overall workplace safety.',
                'short_description': 'AI-powered workplace safety and compliance monitoring solution for factories, warehouses, and offices.',
                'category': 'safety',
                'features': [
                    'Real-time camera monitoring with AI detecting unsafe behaviors (no helmets, spills, hazards)',
                    'Predictive risk analytics based on historical incidents',
                    'Automated compliance reporting for audits and regulators',
                    'Personalized training suggestions for employees based on observed safety habits',
                    'Integration with existing safety management systems',
                    'Real-time alerts and notifications for safety violations',
                    'Comprehensive safety dashboard and analytics'
                ],
                'technologies_used': [
                    'Python', 'OpenCV', 'YOLO', 'Django', 'PostgreSQL', 'Redis', 'Docker', 'Vue.js', 'WebRTC'
                ],
                'client_name': 'ManufacturingPro Corp',
                'project_duration': '7 months',
                'completion_date': date(2023, 6, 30),
                'is_featured': True,
                'is_published': True
            }
        ]
        for solution_data in solutions_data:
            solution = PastSolution.objects.create(**solution_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created past solution: {solution.title}')
            )
        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated {len(solutions_data)} past solutions')
        )