import FWCore.ParameterSet.Config as cms

process = cms.Process('ISPY')

process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.GlobalTag.globaltag = '106X_dataRun2_v37'

# Note: this will replace /store/data in file name
prefix = 'root://eospublic.cern.ch//eos/opendata/cms'

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                'root://eospublic.cern.ch//eos/opendata/cms/Run2016G/DoubleMuon/MINIAOD/UL2016_MiniAODv2-v1/270000/AF85BB29-916D-3C48-86BD-5CA7E832A6A4.root'

                            )
                                ,eventsToProcess = cms.untracked.VEventRange(
                                    '278874:187933819',
                            )
)

process.add_(
    cms.Service("ISpyService",
    outputFileName = cms.untracked.string('fourlepton_miniAOD.ig'),
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



