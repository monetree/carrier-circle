
class HandleError:
    def make_error(traceback,e,fname,exc_type,exc_obj,exc_tb):
        return {
                "code":402,
                "error":e,
                "type":exc_type,
                "line":exc_tb,
                "fname":fname,
                "traceback":traceback
                }
    # def send_mail()
