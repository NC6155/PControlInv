
from .models import Tables
def alerts(request):
    alertsEntries=Tables.objects.all().order_by('stock')
    
    return {"alerts": alertsEntries}