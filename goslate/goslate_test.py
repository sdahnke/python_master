import goslate
import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
gs = goslate.Goslate(executor=executor)
print(gs.translate('hello world', 'de'))