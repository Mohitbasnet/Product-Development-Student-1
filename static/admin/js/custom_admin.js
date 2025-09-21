document.addEventListener('DOMContentLoaded', function() {
    initializeAdminEnhancements();
    addLoadingStates();
    enhanceTableInteractions();
    addRealTimeUpdates();
    initializeTooltips();
});

function initializeAdminEnhancements() {
    addSlideInAnimation();
    enhanceFormValidation();
    addKeyboardShortcuts();
    initializeDashboardWidgets();
}

function addSlideInAnimation() {
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
                if (node.nodeType === 1) {
                    node.classList.add('slide-in');
                }
            });
        });
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
}

function addLoadingStates() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('input[type="submit"], button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.value || submitBtn.textContent;
                submitBtn.innerHTML = '<span class="loading-spinner"></span> Processing...';
                submitBtn.disabled = true;
                
                setTimeout(() => {
                    submitBtn.value = originalText;
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    });
}

function enhanceTableInteractions() {
    const tableRows = document.querySelectorAll('table tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.01)';
            this.style.transition = 'transform 0.2s ease';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
    
    const selectAllCheckbox = document.querySelector('input[name="_selected_action"]');
    if (selectAllCheckbox) {
        selectAllCheckbox.addEventListener('change', function() {
            const checkboxes = document.querySelectorAll('input[name="action"]');
            checkboxes.forEach(checkbox => {
                checkbox.checked = this.checked;
            });
        });
    }
}

function addRealTimeUpdates() {
    updateTimestamps();
    setInterval(updateTimestamps, 60000);
    updateLiveCounters();
    setInterval(updateLiveCounters, 30000);
}

function updateTimestamps() {
    const timeElements = document.querySelectorAll('.time-ago');
    timeElements.forEach(element => {
        const timestamp = element.getAttribute('data-timestamp');
        if (timestamp) {
            const time = new Date(timestamp);
            const now = new Date();
            const diff = now - time;
            
            const minutes = Math.floor(diff / 60000);
            const hours = Math.floor(diff / 3600000);
            const days = Math.floor(diff / 86400000);
            
            let timeString;
            if (days > 0) {
                timeString = `${days} day${days > 1 ? 's' : ''} ago`;
            } else if (hours > 0) {
                timeString = `${hours} hour${hours > 1 ? 's' : ''} ago`;
            } else if (minutes > 0) {
                timeString = `${minutes} minute${minutes > 1 ? 's' : ''} ago`;
            } else {
                timeString = 'Just now';
            }
            
            element.textContent = timeString;
        }
    });
}

function updateLiveCounters() {
    const counters = document.querySelectorAll('.live-counter');
    counters.forEach(counter => {
        counter.classList.add('pulse');
        setTimeout(() => {
            counter.classList.remove('pulse');
        }, 1000);
    });
}

function initializeTooltips() {
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
}

function enhanceFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    
    field.classList.remove('is-valid', 'is-invalid');
    
    if (field.required && !value) {
        field.classList.add('is-invalid');
        showFieldError(field, `${fieldName} is required`);
    } else if (value) {
        field.classList.add('is-valid');
        hideFieldError(field);
    }
    
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            field.classList.add('is-invalid');
            showFieldError(field, 'Please enter a valid email address');
        }
    }
}

function showFieldError(field, message) {
    hideFieldError(field);
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    field.parentNode.appendChild(errorDiv);
}

function hideFieldError(field) {
    const existingError = field.parentNode.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
}

function addKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 's') {
            e.preventDefault();
            const saveBtn = document.querySelector('input[name="_save"]');
            if (saveBtn) {
                saveBtn.click();
            }
        }
        
        if (e.ctrlKey && e.key === 'n') {
            e.preventDefault();
            const addBtn = document.querySelector('.addlink');
            if (addBtn) {
                addBtn.click();
            }
        }
        
        if (e.key === 'Escape') {
            const backBtn = document.querySelector('.historylink');
            if (backBtn) {
                backBtn.click();
            }
        }
    });
}

function initializeDashboardWidgets() {
    addQuickActions();
}

function addQuickActions() {
    const content = document.querySelector('.content');
    if (content) {
        const quickActionsHTML = `
            <div class="card">
                <div class="card-header">
                    <h3 class="card-title">Quick Actions</h3>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-3">
                            <a href="/admin/contact/contactinquiry/add/" class="btn btn-primary btn-block">
                                <i class="fas fa-plus"></i> New Inquiry
                            </a>
                        </div>
                        <div class="col-md-3">
                            <a href="/admin/news/article/add/" class="btn btn-success btn-block">
                                <i class="fas fa-edit"></i> New Article
                            </a>
                        </div>
                        <div class="col-md-3">
                            <a href="/admin/events/event/add/" class="btn btn-warning btn-block">
                                <i class="fas fa-calendar-plus"></i> New Event
                            </a>
                        </div>
                        <div class="col-md-3">
                            <a href="/admin/testimonials/testimonial/add/" class="btn btn-info btn-block">
                                <i class="fas fa-quote-left"></i> New Testimonial
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        `;
        content.insertAdjacentHTML('beforeend', quickActionsHTML);
    }
}

const style = document.createElement('style');
style.textContent = `
    .pulse {
        animation: pulse 1s ease-in-out;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .activity-feed {
        max-height: 300px;
        overflow-y: auto;
    }
    
    .activity-item {
        display: flex;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #eee;
    }
    
    .activity-item i {
        margin-right: 10px;
        width: 20px;
    }
    
    .activity-item span {
        flex: 1;
        margin-right: 10px;
    }
    
    .activity-item small {
        color: #666;
    }
    
    .btn-block {
        width: 100%;
        margin-bottom: 10px;
    }
`;
document.head.appendChild(style);
