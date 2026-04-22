import { useState } from 'react';
import { Copy, Check } from 'lucide-react';
import TransparencyBadge from './TransparencyBadge';

export default function BadgePreview({ result, brandName }: { result: any, brandName: string }) {
    const [copied, setCopied] = useState(false);
    const embedCode = `<div id="verilabel-badge" data-id="${result.report_id}"></div>\n<script src="https://cdn.verilabel.ai/v1/badge.js"></script>`;

    const copyToClipboard = () => {
        navigator.clipboard.writeText(embedCode);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <div className="mt-8 pt-8 border-t border-slate-200">
            <h3 className="text-lg font-semibold mb-4">Transparency Badge Preview</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">

                {/* Visual Preview */}
                <div className="flex justify-center p-8 bg-slate-100 rounded-xl border border-dashed border-slate-300">
                    <TransparencyBadge
                        status={result.status}
                        brandName={brandName}
                        date={new Date().toLocaleDateString()}
                    />
                </div>

                {/* Embed Snippet */}
                <div className="bg-slate-900 rounded-lg p-4 relative">
                    <label className="text-xs text-slate-400 mb-2 block uppercase font-bold">Embed Snippet</label>
                    <code className="text-emerald-400 text-xs break-all leading-relaxed">
                        {embedCode}
                    </code>
                    <button
                        onClick={copyToClipboard}
                        className="absolute top-4 right-4 text-slate-400 hover:text-white transition-colors"
                    >
                        {copied ? <Check size={18} className="text-emerald-400" /> : <Copy size={18} />}
                    </button>
                </div>
            </div>
        </div>
    );
}