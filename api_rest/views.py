
# Views

## Login
from .auth.login import LoginAPI

### WhatsApp Variables
from .view.WhatsappVars import whatsapp_variables_get, create_whatsapp_variables, update_whatsapp_variables, delete_whatsapp_variables

## Contatos
from .view.Contatos import get_contacts, contact_create, contact_update, contact_delete

## Mensagens
from .view.Mensagens import get_messages, message_create, message_update, message_delete

## Kanban
from .view.Kanban import get_contact_kanban, create_contact_kanban, update_contact_kanban, delete_contact_kanban

## Dashboard
from .view.Dashboard import dashboard_stats, dashboard_users

