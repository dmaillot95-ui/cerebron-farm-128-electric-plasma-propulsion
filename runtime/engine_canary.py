import json,math,hashlib,pathlib,platform
# Electric propulsion engineering canary: ion exhaust, thrust, beam current and ideal efficiency consistency.
e=1.602176634e-19; amu=1.66053906660e-27; m_i=131.293*amu; V=1000.; mdot=5e-6; eta=0.65; P=5000.
ve=math.sqrt(2*e*V/m_i); thrust=mdot*ve; isp=ve/9.80665; ion_rate=mdot/m_i; beam_current=ion_rate*e; jet_power=.5*mdot*ve**2; eff=jet_power/P
# Identity checks from the same declared idealized ion model.
ok=20000<ve<50000 and .05<thrust<.3 and 1000<isp<5000 and beam_current>0 and abs(jet_power-mdot*e*V/m_i)<1e-9*jet_power
out={"farm":128,"engine":"python-electric-ion-propulsion-canary","engine_version":platform.python_version(),"test":"XENON_1KV_IDEAL_ION_BEAM","xenon_ion_mass_kg":m_i,"beam_voltage_v":V,"mass_flow_kg_s":mdot,"input_power_w":P,"exhaust_velocity_m_s":ve,"thrust_n":thrust,"isp_s":isp,"beam_current_a":beam_current,"jet_power_w":jet_power,"jet_power_over_input":eff,"declared_efficiency_context":eta,"status":"REAL_ENGINE_CANARY_OK" if ok else "FAIL","epistemic_status":"IDEAL_ION_ENGINEERING_CANARY_NOT_PIC_HALL_THRUSTER_OR_HARDWARE_VALIDATION"}
raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f128_engine_canary.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
