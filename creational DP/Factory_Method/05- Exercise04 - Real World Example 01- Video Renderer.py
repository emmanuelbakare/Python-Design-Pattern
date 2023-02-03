class VideoRenderer:
    def __init__(self, video_type):
        self._video_type = video_type 

    def render(self):
        pass

class MP4Renderer(VideoRenderer):
    def render(self):
        print("Rendering video in MP4 format")

class AVIRenderer(VideoRenderer):
    def render(self):
        print("Rendering video in AVI format")
        
class MKVRenderer(VideoRenderer):
    def render(self):
        print("Rendering video in MKV format")

class VideoRendererFactory:
    def __init__(self):
        self._renderers = dict(mp4=MP4Renderer, avi=AVIRenderer, mkv=MKVRenderer)
    
    @property 
    def renderers(self):
        return self._renderers

    def get_renderer(self, video_type):
        return self._renderers[video_type](video_type)

def main():
    factory =  VideoRendererFactory()
    render_list = ", ".join(factory.renderers)
    while True:

        renderer_type = input(f"Enter a renderer ({render_list}): ")
        if renderer_type in factory.renderers:
            break
        print(f"This Renderer does not exist : TRY AGAIN ({render_list}) ")
    
    codec = factory.get_renderer(renderer_type)
    codec.render()

if __name__ == "__main__":
    main()
