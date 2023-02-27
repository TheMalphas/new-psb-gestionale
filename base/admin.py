from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.apps import apps
from . import models as mo
import zipfile
import qrcode
from PIL import Image, ImageDraw, ImageFont, PSDraw
from io import BytesIO


# Register your models here.
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

class DownloadAllQr(admin.ModelAdmin):
    model = mo.AppoggioVerificaQr.objects.all()
    fields = "__all__"
    
    actions = ["print_all"]
    def print(self, request):
        dati = mo.AppoggioVerificaQr.objects.all()
        with zipfile.ZipFile("QR_Codes.zip", "w", compression=zipfile.ZIP_DEFLATED) as z:
            response = HttpResponse(content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename=QR_Codes.zip'
            for el in dati:
                qr = qrcode.QRCode(
                    version=1,
                    box_size=6,
                    border=10
                )
                qr.add_data(el.uuid_qr)
                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color=(255, 255, 255))
                
                font_size = 16
                font = ImageFont.truetype("Roboto-Bold.ttf", size=font_size)
                
                text = el.id_dipendente.nominativo.upper()
                text_width, text_height = font.getsize(text)
                border_size = qr.border * qr.box_size
                center_x = (qr.modules_count * qr.box_size) / 1.25
                center_y = (qr.modules_count * qr.box_size) / 0.95
                
                draw = ImageDraw.Draw(img)
                draw.text((center_x - text_width / 2, center_y + border_size + 10), text, (0, 0, 0), font=font, align='center')
                
                buffer = BytesIO()
                img.save(buffer, format='PNG')
                z.write(img)
            response.write(buffer.getvalue())
                
            return response