from django import forms
from django.utils.safestring import mark_safe
import json

class FeaturesWidget(forms.Textarea):
    """Custom widget for features field with JSON validation and better UX"""
    
    def __init__(self, attrs=None):
        default_attrs = {'rows': 5, 'cols': 50}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
    
    def render(self, name, value, attrs=None, renderer=None):
        # Convert JSON string to list for display
        if value:
            try:
                features_list = json.loads(value) if isinstance(value, str) else value
                if isinstance(features_list, list):
                    value = '\n'.join(features_list)
            except (json.JSONDecodeError, TypeError):
                pass
        
        # Add help text
        help_text = """
        <div class="help">
            <p><strong>Instructions:</strong></p>
            <ul>
                <li>Enter one feature per line</li>
                <li>Features will be automatically formatted as a JSON list</li>
                <li>Example:</li>
            </ul>
            <pre>Natural Language Processing
24/7 Availability
Multi-language Support
Learning Capabilities</pre>
        </div>
        """
        
        # Render the textarea
        textarea = super().render(name, value, attrs, renderer)
        
        return mark_safe(f'{textarea}{help_text}')
    
    def value_from_datadict(self, data, files, name):
        value = data.get(name, '')
        if value:
            # Convert newline-separated text to JSON list
            features_list = [feature.strip() for feature in value.split('\n') if feature.strip()]
            return json.dumps(features_list)
        return '[]'
