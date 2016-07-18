import ROOT
import os
import uuid

def awesome_plot(canv, name='q', pos='topright', return_canvas=False):

    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    file_name = os.path.join(dir_name, 'signature_%s.gif' % name)
    img = ROOT.TImage.Open(file_name)

    if pos != 'topright':
        print 'sorry need to implement other positions'
    pad_name = uuid.uuid4().hex
    pad = ROOT.TPad(
        pad_name, pad_name,
        0.8, 1 - canv.GetTopMargin() - 0.2,
        1 - canv.GetRightMargin() - 0.02,
        1 - canv.GetTopMargin() - 0.02)
    pad.Draw()
    pad.cd()
    img.Draw()
    canv.Update()
    if return_canvas:
        return canv
