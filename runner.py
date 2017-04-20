import celery
import locale
import os
import subprocess
import tempfile

import time


app = celery.Celery('runner')
app.conf.broker_url = os.environ.get('BROKER', 'pyamqp://')
app.conf.result_backend = os.environ.get('BACKEND', 'redis://')

encoding = locale.getdefaultlocale()[1]

@app.task
def run(task_id, source_code):
    f = tempfile.NamedTemporaryFile(mode='w')
    f.write(source_code)
    f.flush()
    p = subprocess.Popen(['python3', f.name],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = p.communicate()
    f.close()
    subprocess.call(['celery', 'control', 'shutdown'])
    return {'task_id': task_id,
            'stdout': stdoutdata.decode(encoding),
            'stderr': stderrdata.decode(encoding),
            'exit_code': p.returncode}
