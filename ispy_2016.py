import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from FWCore.MessageLogger.MessageLogger_cfi import *

process = cms.Process("process", Run2_2018)

process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# Note: this will replace /store/data in file name
prefix = 'root://eospublic.cern.ch//eos/opendata/cms'

import FWCore.Utilities.FileUtils as FileUtils

#files = FileUtils.loadListFromFile("DoubleMu_2016G.txt")
#files = FileUtils.loadListFromFile("DoubleEG_2016G.txt")
#files = FileUtils.loadListFromFile("DoubleMu_2016H.txt")
files = FileUtils.loadListFromFile("DoubleEG_2016H.txt")

newfiles = [f.replace('/store/data', prefix) for f in files]

run_events = FileUtils.loadListFromFile("run_event.txt")

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(*newfiles),
    eventsToProcess = cms.untracked.VEventRange(*run_events)
)

process.add_(
    cms.Service("ISpyService",
    outputFileName = cms.untracked.string('DoubleEG2016H.ig'),
    outputMaxEvents = cms.untracked.int32(50)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.load("ISpy.Analyzers.ISpyEvent_cfi")
process.load('ISpy.Analyzers.ISpyEBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyEERecHit_cfi')
process.load('ISpy.Analyzers.ISpyESRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHERecHit_cfi')
process.load('ISpy.Analyzers.ISpyHFRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHORecHit_cfi')
process.load('ISpy.Analyzers.ISpyPATMuon_cfi')
process.load('ISpy.Analyzers.ISpyPATElectron_cfi')
process.load('ISpy.Analyzers.ISpyPackedCandidate_cfi')
process.load('ISpy.Analyzers.ISpyVertex_cfi')
process.load('ISpy.Analyzers.ISpyPATJet_cfi')
process.load('ISpy.Analyzers.ISpyPATMET_cfi')

process.ISpyEBRecHit.iSpyEBRecHitTag = cms.InputTag('reducedEgamma:reducedEBRecHits')
process.ISpyEERecHit.iSpyEERecHitTag = cms.InputTag('reducedEgamma:reducedEERecHits')
process.ISpyESRecHit.iSpyESRecHitTag = cms.InputTag('reducedEgamma:reducedESRecHits')
process.ISpyHBRecHit.iSpyHBRecHitTag = cms.InputTag("reducedEgamma:reducedHBHEHits")
process.ISpyHERecHit.iSpyHERecHitTag = cms.InputTag("reducedEgamma:reducedHBHEHits")
process.ISpyHFRecHit.iSpyHFRecHitTag = cms.InputTag("slimmedHcalRecHits:reducedHcalRecHits")
process.ISpyHORecHit.iSpyHORecHitTag = cms.InputTag("slimmedHcalRecHits:reducedHcalRecHits")
process.ISpyPATMuon.iSpyPATMuonTag = cms.InputTag("slimmedMuons")
process.ISpyPATElectron.iSpyPATElectronTag = cms.InputTag("slimmedElectrons")
process.ISpyPackedCandidate.iSpyPackedCandidateTag = cms.InputTag('packedPFCandidates')
process.ISpyPATJet.iSpyPATJetTag = cms.InputTag('slimmedJets')
process.ISpyPATMET.iSpyPATMETTag = cms.InputTag('slimmedMETs')
process.ISpyVertex.iSpyPriVertexTag = cms.InputTag('offlineSlimmedPrimaryVertices')

process.iSpy = cms.Path(process.ISpyEvent*
                        process.ISpyEBRecHit*
                        process.ISpyEERecHit*
                        process.ISpyESRecHit*
                        process.ISpyHBRecHit*
                        process.ISpyHERecHit*
                        process.ISpyHFRecHit*
                        process.ISpyHORecHit*
                        process.ISpyPATMuon*
                        process.ISpyPATElectron*
                        process.ISpyPATJet*
                        process.ISpyPATMET*
                        process.ISpyPackedCandidate*
                        process.ISpyVertex)

process.schedule = cms.Schedule(process.iSpy)



