#!/usr/bin/env python
import ROOT
try:
    from rootpy.plotting.style import set_style
    set_style('ATLAS', shape='rect')
except:
    print 'you should try rootpy, it is nice'



if __name__ == '__main__':
    
    from argparse import ArgumentParser
    parser = ArgumentParser('-a', '--autograph', default=False, action='store_true')

    args.parse_args()

    ROOT.gROOT.SetBatch(True)

    canv = ROOT.TCanvas()
    h1 = ROOT.TH1F("h1", "h1", 100, -5, 5)
    h1.FillRandom('gaus', 10000)
    h1.GetXaxis().SetTitle('X')
    h1.GetYaxis().SetTitle('Number of events')
    h1.Draw()

    if args.autograph:
        from img import awesome_plot
        awesome_plot(canv)
        canv.SaveAs('awesome_plot.png')
    else:
        canv.SaveAs('lame_plot.png')

