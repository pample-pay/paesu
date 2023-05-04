# Generated by Django 4.1.7 on 2023-04-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_remove_paesu_record_유저 기록 unique key_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paesu_record',
            name='diswaste_ck',
        ),
        migrations.AlterField(
            model_name='paesu_record',
            name='emission_end',
            field=models.CharField(choices=[('01:00', '1시'), ('02:00', '2시'), ('03:00', '3시'), ('04:00', '4시'), ('05:00', '5시'), ('06:00', '6시'), ('07:00', '7시'), ('08:00', '8시'), ('09:00', '9시'), ('10:00', '10시'), ('11:00', '11시'), ('12:00', '12시'), ('13:00', '13시'), ('14:00', '14시'), ('15:00', '15시'), ('16:00', '16시'), ('17:00', '17시'), ('18:00', '18시'), ('19:00', '19시'), ('20:00', '20시'), ('21:00', '21시'), ('22:00', '22시'), ('23:00', '23시'), ('24:00', '24시')], default=18, max_length=10, verbose_name='배출시설 가동 종료시간'),
        ),
        migrations.AlterField(
            model_name='paesu_record',
            name='emission_start',
            field=models.CharField(choices=[('01:00', '1시'), ('02:00', '2시'), ('03:00', '3시'), ('04:00', '4시'), ('05:00', '5시'), ('06:00', '6시'), ('07:00', '7시'), ('08:00', '8시'), ('09:00', '9시'), ('10:00', '10시'), ('11:00', '11시'), ('12:00', '12시'), ('13:00', '13시'), ('14:00', '14시'), ('15:00', '15시'), ('16:00', '16시'), ('17:00', '17시'), ('18:00', '18시'), ('19:00', '19시'), ('20:00', '20시'), ('21:00', '21시'), ('22:00', '22시'), ('23:00', '23시'), ('24:00', '24시')], default=9, max_length=10, verbose_name='배출시설가동 시작시간'),
        ),
        migrations.AlterField(
            model_name='paesu_record',
            name='op_end',
            field=models.CharField(choices=[('01:00', '1시'), ('02:00', '2시'), ('03:00', '3시'), ('04:00', '4시'), ('05:00', '5시'), ('06:00', '6시'), ('07:00', '7시'), ('08:00', '8시'), ('09:00', '9시'), ('10:00', '10시'), ('11:00', '11시'), ('12:00', '12시'), ('13:00', '13시'), ('14:00', '14시'), ('15:00', '15시'), ('16:00', '16시'), ('17:00', '17시'), ('18:00', '18시'), ('19:00', '19시'), ('20:00', '20시'), ('21:00', '21시'), ('22:00', '22시'), ('23:00', '23시'), ('24:00', '24시')], default=18, max_length=10, verbose_name='운영종료시간'),
        ),
        migrations.AlterField(
            model_name='paesu_record',
            name='op_start',
            field=models.CharField(choices=[('01:00', '1시'), ('02:00', '2시'), ('03:00', '3시'), ('04:00', '4시'), ('05:00', '5시'), ('06:00', '6시'), ('07:00', '7시'), ('08:00', '8시'), ('09:00', '9시'), ('10:00', '10시'), ('11:00', '11시'), ('12:00', '12시'), ('13:00', '13시'), ('14:00', '14시'), ('15:00', '15시'), ('16:00', '16시'), ('17:00', '17시'), ('18:00', '18시'), ('19:00', '19시'), ('20:00', '20시'), ('21:00', '21시'), ('22:00', '22시'), ('23:00', '23시'), ('24:00', '24시')], default=9, max_length=10, verbose_name='운영시작시간'),
        ),
        migrations.AlterField(
            model_name='paesu_record',
            name='poweruse_end',
            field=models.CharField(choices=[('01:00', '1시'), ('02:00', '2시'), ('03:00', '3시'), ('04:00', '4시'), ('05:00', '5시'), ('06:00', '6시'), ('07:00', '7시'), ('08:00', '8시'), ('09:00', '9시'), ('10:00', '10시'), ('11:00', '11시'), ('12:00', '12시'), ('13:00', '13시'), ('14:00', '14시'), ('15:00', '15시'), ('16:00', '16시'), ('17:00', '17시'), ('18:00', '18시'), ('19:00', '19시'), ('20:00', '20시'), ('21:00', '21시'), ('22:00', '22시'), ('23:00', '23시'), ('24:00', '24시')], default=18, max_length=10, verbose_name='전산전력계지침 가동 종료시간'),
        ),
        migrations.AlterField(
            model_name='paesu_record',
            name='poweruse_start',
            field=models.CharField(choices=[('01:00', '1시'), ('02:00', '2시'), ('03:00', '3시'), ('04:00', '4시'), ('05:00', '5시'), ('06:00', '6시'), ('07:00', '7시'), ('08:00', '8시'), ('09:00', '9시'), ('10:00', '10시'), ('11:00', '11시'), ('12:00', '12시'), ('13:00', '13시'), ('14:00', '14시'), ('15:00', '15시'), ('16:00', '16시'), ('17:00', '17시'), ('18:00', '18시'), ('19:00', '19시'), ('20:00', '20시'), ('21:00', '21시'), ('22:00', '22시'), ('23:00', '23시'), ('24:00', '24시')], default=9, max_length=10, verbose_name='전산전력계지침 가동 시작시간'),
        ),
        migrations.AlterField(
            model_name='paesu_record',
            name='prev_end',
            field=models.CharField(choices=[('01:00', '1시'), ('02:00', '2시'), ('03:00', '3시'), ('04:00', '4시'), ('05:00', '5시'), ('06:00', '6시'), ('07:00', '7시'), ('08:00', '8시'), ('09:00', '9시'), ('10:00', '10시'), ('11:00', '11시'), ('12:00', '12시'), ('13:00', '13시'), ('14:00', '14시'), ('15:00', '15시'), ('16:00', '16시'), ('17:00', '17시'), ('18:00', '18시'), ('19:00', '19시'), ('20:00', '20시'), ('21:00', '21시'), ('22:00', '22시'), ('23:00', '23시'), ('24:00', '24시')], default=18, max_length=10, verbose_name='방지시설 가동 종료시간'),
        ),
        migrations.AlterField(
            model_name='paesu_record',
            name='prev_start',
            field=models.CharField(choices=[('01:00', '1시'), ('02:00', '2시'), ('03:00', '3시'), ('04:00', '4시'), ('05:00', '5시'), ('06:00', '6시'), ('07:00', '7시'), ('08:00', '8시'), ('09:00', '9시'), ('10:00', '10시'), ('11:00', '11시'), ('12:00', '12시'), ('13:00', '13시'), ('14:00', '14시'), ('15:00', '15시'), ('16:00', '16시'), ('17:00', '17시'), ('18:00', '18시'), ('19:00', '19시'), ('20:00', '20시'), ('21:00', '21시'), ('22:00', '22시'), ('23:00', '23시'), ('24:00', '24시')], default=9, max_length=10, verbose_name='방지시설가동 시작시간'),
        ),
    ]
