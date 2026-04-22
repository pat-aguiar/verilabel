import { useState } from 'react';
import { Upload, CheckCircle, XCircle, Beaker, FileText } from 'lucide-react';
import { uploadReport } from '../services/api';
import BadgePreview from './BadgePreview';

export default function Dashboard() {
    const [file, setFile] = useState<File | null>(null);
    const [brandName, setBrandName] = useState('');
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<any>(null);

    const handleUpload = async () => {
        if (!file || !brandName) return;
        setLoading(true);
        try {
            const data = await uploadReport(brandName, file);
            setResult(data);
        } catch (error) {
            console.error("Upload failed", error);
            alert("Error processing PDF. Check console.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-slate-50 p-8">
            <header className="mb-8">
                <h1 className="text-3xl font-bold text-slate-900">VeriLabel Dashboard</h1>
                <p className="text-slate-500">Automated CPG Compliance Engine</p>
            </header>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Upload Section */}
                <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                    <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                        <Upload size={20} /> Ingest Lab Report
                    </h2>
                    <div className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-slate-700">Brand Name</label>
                            <input
                                type="text"
                                className="w-full mt-1 p-2 border rounded-md"
                                placeholder="e.g. Terra Organics"
                                value={brandName}
                                onChange={(e) => setBrandName(e.target.value)}
                            />
                        </div>
                        <div className="border-2 border-dashed border-slate-300 rounded-lg p-8 text-center hover:border-veri-green transition-colors">
                            <input
                                type="file"
                                id="pdf-upload"
                                className="hidden"
                                accept=".pdf"
                                onChange={(e) => setFile(e.target.files?.[0] || null)}
                            />
                            <label htmlFor="pdf-upload" className="cursor-pointer">
                                <FileText className="mx-auto mb-2 text-slate-400" size={40} />
                                <span className="text-sm text-slate-600">
                                    {file ? file.name : "Click to upload lab PDF"}
                                </span>
                            </label>
                        </div>
                        <button
                            onClick={handleUpload}
                            disabled={loading || !file}
                            className="w-full bg-slate-900 text-white py-2 rounded-md hover:bg-slate-800 disabled:opacity-50 transition-all"
                        >
                            {loading ? "AI is Analyzing..." : "Run Compliance Check"}
                        </button>
                    </div>
                </div>

                {/* Results Section */}
                <div className="lg:col-span-2 bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                    <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                        <Beaker size={20} /> Analysis Results
                    </h2>

                    {result ? (
                        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
                            <div className={`mb-6 p-4 rounded-lg flex items-center gap-3 ${result.status === 'compliant' ? 'bg-emerald-50 text-emerald-700' : 'bg-rose-50 text-rose-700'
                                }`}>
                                {result.status === 'compliant' ? <CheckCircle /> : <XCircle />}
                                <span className="font-bold uppercase tracking-wider">
                                    Status: {result.status}
                                </span>
                            </div>

                            <table className="w-full text-left">
                                <thead>
                                    <tr className="text-slate-500 text-sm border-b">
                                        <th className="pb-2">Analyte</th>
                                        <th className="pb-2 text-right">Detected (PPM)</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {Object.entries(result.data).map(([chemical, value]: [string, any]) => (
                                        <tr key={chemical} className="border-b last:border-0">
                                            <td className="py-3 capitalize text-slate-700 font-medium">{chemical}</td>
                                            <td className="py-3 text-right font-mono">{value}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                            <BadgePreview result={result} brandName={brandName} />
                        </div>
                    ) : (
                        <div className="h-64 flex flex-col items-center justify-center text-slate-400">
                            <p>No report processed yet.</p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}