from flask import Flask,jsonify
import isl
app=Flask(__name__)

@app.route('/')
def hello_world():
    # num=isl.sum(2,4)
    return 'num'
@app.route('/islframing/<string:n>')
def frame(n):
    isl_framed_sentence=isl.isl_framing(n)
    available = isl.list_of_available_sarthak(isl_framed_sentence)
    videos = [video + ".mp4" for video in available]
    result={
        'Original':n,
        'isl_framed': isl_framed_sentence,
        'video_list':videos
    }
    return result
if __name__=='__main__':
    app.run(debug=True)
