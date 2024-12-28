SYSTEM_PROMPT = """You are an expert annotator specializing in electrical engineering NER tagging. For each request, generate a unique and diverse sentence covering different aspects of electrical engineering, such as circuit design, testing, maintenance, installation, troubleshooting, or research."""

USER_PROMPT = """Generate one unique electrical engineering sentence with NER tags in JSON format. Each generated sentence should be different by:
1. Using different combinations of components, parameters, and entities
2. Varying sentence structures and technical scenarios
3. Covering different aspects: design, testing, measurement, maintenance, research
4. Including various technical activities: analyzing, measuring, designing, testing, debugging


NER Tag Definitions:
{
    "B-COMPONENT": "Start of electronic parts - (e.g. Resistors, Capacitors, Inductors, Transformers, Diodes, Transistors, MOSFETs, Op-Amps)",
    "I-COMPONENT": "Continuation of component",
    "B-DESIGN_PARAM": "Start of measurements - (e.g. Voltage, Current, Power, Frequency, Resistance, Capacitance, Inductance)",
    "I-DESIGN_PARAM": "Continuation of parameter",
    "B-MATERIAL": "Start of materials - (e.g. Silicon, Gallium Arsenide, Copper, Aluminum, Insulators, Conductors)",
    "I-MATERIAL": "Continuation of material",
    "B-EQUIPMENT": "Start of test equipment - (e.g. Oscilloscope, Multimeter, Spectrum Analyzer, Soldering Iron, Power Supply)",
    "I-EQUIPMENT": "Continuation of equipment",
    "B-TECHNOLOGY": "Start of systems - (e.g. Microcontrollers, Microprocessors, FPGA, ASIC, Embedded Systems)",
    "I-TECHNOLOGY": "Continuation of technology",
    "B-SOFTWARE": "Start of software tools - (e.g., MATLAB, LTSpice)",
    "I-SOFTWARE": "Continuation of software",
    "B-STANDARD": "Start of protocols/standards - (e.g. IEEE 802.11, USB 3.0, RS-232, ISO 9001)",
    "I-STANDARD": "Continuation of standard",
    "B-VENDOR": "Start of manufacturer names - (e.g. Tektronix, Texas Instruments)",
    "I-VENDOR": "Continuation of vendor",
    "B-PRODUCT": "Start of product names - (e.g., Arduino, Raspberry Pi)",
    "I-PRODUCT": "Continuation of product",
    "O": "Non-entity tokens"
}

Rules:
1. Generate exactly one sentence
2. Include at least 2 different entity types
3. Use proper BIO tagging
4. Keep measurements as single tokens

Required Output Structure:
{
    "sentence": "Complete sentence here",
    "annotations": [
        {
            "token": "word1",
            "tag": "TAG1"
        },
        {
            "token": "word2",
            "tag": "TAG2"
        }
    ]
}

Example Output:
{
    "sentence": "The LM324 op-amp requires a 5V DC power supply.",
    "annotations": [
        {
            "token": "The",
            "tag": "O"
        },
        {
            "token": "LM324",
            "tag": "B-PRODUCT"
        },
        {
            "token": "op",
            "tag": "B-COMPONENT"
        },
        {
            "token": "amp",
            "tag": "I-COMPONENT"
        },
        {
            "token": "requires",
            "tag": "O"
        },
        {
            "token": "a",
            "tag": "O"
        },
        {
            "token": "5V",
            "tag": "B-DESIGN_PARAM"
        },
        {
            "token": "DC",
            "tag": "O"
        },
        {
            "token": "power",
            "tag": "O"
        },
        {
            "token": "supply",
            "tag": "O"
        },
        {
            "token": ".",
            "tag": "O"
        }
    ]
}

Generate one new example following this exact JSON structure. Ensure the sentence is different from previous examples and combines multiple technical aspects."""
