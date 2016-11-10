# -*- encoding:utf-8 -*-
import psutil
def cpu():
    cpu=psutil.cpu_percent(0.1);
    return cpu

def mem():
    meminfo = psutil.virtual_memory();
    mem = (meminfo.total - meminfo.available) / meminfo.total * 100;
    return mem

