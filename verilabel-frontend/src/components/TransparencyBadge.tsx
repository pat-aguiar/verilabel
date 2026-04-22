import { ShieldCheck, AlertTriangle } from 'lucide-react';

interface BadgeProps {
    status: 'compliant' | 'non-compliant';
    brandName: string;
    date: string;
}

export default function TransparencyBadge({ status, brandName, date }: BadgeProps) {
    const isPass = status === 'compliant';

    return (
        <div className={`flex items-center gap-4 p-4 rounded-2xl border-2 max-w-sm transition-all duration-500 ${isPass
                ? 'bg-emerald-50 border-emerald-200 text-emerald-900 shadow-sm'
                : 'bg-rose-50 border-rose-200 text-rose-900'
            }`}>
            <div className={`p-3 rounded-full ${isPass ? 'bg-emerald-500' : 'bg-rose-500'}`}>
                {isPass ? <ShieldCheck className="text-white" size={28} /> : <AlertTriangle className="text-white" size={28} />}
            </div>

            <div>
                <div className="flex items-center gap-2">
                    <span className="font-bold text-lg uppercase tracking-tight">VeriLabel</span>
                    <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold uppercase ${isPass ? 'bg-emerald-200 text-emerald-700' : 'bg-rose-200 text-rose-700'
                        }`}>
                        {isPass ? 'Verified' : 'Flagged'}
                    </span>
                </div>
                <p className="text-sm opacity-80 leading-tight">
                    {isPass
                        ? `${brandName} meets Prop 65 safety standards.`
                        : `${brandName} exceeds chemical safety thresholds.`}
                </p>
                <p className="text-[10px] mt-1 opacity-50 font-mono">ID: {date}</p>
            </div>
        </div>
    );
}