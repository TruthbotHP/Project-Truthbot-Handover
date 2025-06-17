
from flask import Blueprint, request, jsonify
from core.hp_siip_scorer import HPSIIPScorer
from core.vpdf_reflection_logger import VPDFLogger
from core.deductive_fractal_trace import DeductiveFractalTracer

router = Blueprint('router', __name__)

scorer = HPSIIPScorer()
logger = VPDFLogger()
tracer = DeductiveFractalTracer()

@router.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    phrase = data.get("text", "")
    result = scorer.score_phrase(phrase)

    # Extract first flagged term or symbol for tracing
    target_symbol = result["flags"][0]["word"] if result["flags"] else ""
    trace_output = tracer.trace_symbol(target_symbol) if target_symbol else []

    logger.log_reflection(phrase, result)

    return jsonify({
        "original_phrase": phrase,
        "scoring_result": result,
        "symbolic_trace": trace_output
    })

@router.route("/symbols", methods=["GET"])
def list_symbols():
    return jsonify({"symbols": scorer.symbolic_map})

@router.route("/log", methods=["GET"])
def get_log():
    return logger.get_latest()
