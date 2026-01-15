#!/usr/bin/env python3
"""
THRESHOLD_ONSET — Main Entry Point

Phase 0: Action before Knowledge
कार्य (kārya) happens before ज्ञान (jñāna)
"""

import sys
from pathlib import Path

# Add src directory to path for proper imports
project_root = Path(__file__).parent
src_dir = project_root / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))


def run_phase0_noise_baseline():
    """
    Run Phase 0 pipeline — NOISE BASELINE (FROZEN).
    
    Pure random actions with no structure.
    This is the baseline that proves: random → no persistence.

    Phase 0 produces ONLY:
    - Total residue count
    - Unique residue count
    - Collision rate

    Nothing else is allowed.
    """
    # Import here after path setup (intentional)
    from phase0.phase0 import phase0  # pylint: disable=import-outside-toplevel,import-error
    import random  # pylint: disable=import-outside-toplevel

    # Raw actions - pure noise, no structure
    # No strings, no labels, no meaning
    # Just raw action residues
    # Using lambda to create callables (required for actions)
    actions = [
        lambda: random.random(),  # pylint: disable=unnecessary-lambda
        lambda: random.random(),  # pylint: disable=unnecessary-lambda
    ]

    steps = 100  # Increased temporal depth to test persistence

    # Collect traces
    traces = []
    for trace, _, _ in phase0(actions, steps=steps):
        traces.append(trace)

    # Calculate canonical Phase 0 outputs ONLY
    total_count = len(traces)
    unique_count = len(set(traces))
    collision_rate = 1.0 - (unique_count / total_count) if total_count > 0 else 0.0

    # Output canonical Phase 0 results ONLY
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 0 (Noise Baseline)")
    print("=" * 70)
    print()
    print("Total residue count:    ", total_count)
    print("Unique residue count:    ", unique_count)
    print("Collision rate:          ", f"{collision_rate:.4f}")
    print()
    print("=" * 70)

    return traces


def run_phase0_inertia():
    """
    Run Phase 0 pipeline — INERTIA VARIANT.
    
    Actions with temporal correlation: Action(t+1) depends weakly on Action(t).
    Still Phase 0 compliant: numeric, opaque, no meaning.
    """
    # Import here after path setup (intentional)
    from phase0.phase0 import phase0  # pylint: disable=import-outside-toplevel,import-error
    from phase0.actions import InertiaAction  # pylint: disable=import-outside-toplevel,import-error

    # Stateful action with carry-over (internal state, no naming)
    actions = [
        InertiaAction(),
        InertiaAction(),
    ]

    steps = 100  # Increased temporal depth to test persistence

    # Collect traces
    traces = []
    for trace, _, _ in phase0(actions, steps=steps):
        traces.append(trace)

    # Calculate canonical Phase 0 outputs ONLY
    total_count = len(traces)
    unique_count = len(set(traces))
    collision_rate = 1.0 - (unique_count / total_count) if total_count > 0 else 0.0

    # Output canonical Phase 0 results ONLY
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 0 (Inertia Variant)")
    print("=" * 70)
    print()
    print("Total residue count:    ", total_count)
    print("Unique residue count:    ", unique_count)
    print("Collision rate:          ", f"{collision_rate:.4f}")
    print()
    print("=" * 70)

    return traces


def run_phase0_random_walk():
    """
    Run Phase 0 pipeline — RANDOM WALK VARIANT.
    
    Bounded random walk: Action drifts within bounds.
    Still Phase 0 compliant: numeric, opaque, no meaning.
    """
    # Import here after path setup (intentional)
    from phase0.phase0 import phase0  # pylint: disable=import-outside-toplevel,import-error
    from phase0.actions import BoundedWalk  # pylint: disable=import-outside-toplevel,import-error

    # Position is internal state, not named
    actions = [
        BoundedWalk(),
        BoundedWalk(),
    ]

    steps = 100  # Increased temporal depth to test persistence

    # Collect traces
    traces = []
    for trace, _, _ in phase0(actions, steps=steps):
        traces.append(trace)

    # Calculate canonical Phase 0 outputs ONLY
    total_count = len(traces)
    unique_count = len(set(traces))
    collision_rate = 1.0 - (unique_count / total_count) if total_count > 0 else 0.0

    # Output canonical Phase 0 results ONLY
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 0 (Random Walk Variant)")
    print("=" * 70)
    print()
    print("Total residue count:    ", total_count)
    print("Unique residue count:    ", unique_count)
    print("Collision rate:          ", f"{collision_rate:.4f}")
    print()
    print("=" * 70)

    return traces


def run_phase0_oscillator():
    """
    Run Phase 0 pipeline — OSCILLATOR VARIANT.
    
    Weak oscillator: Action oscillates with noise.
    Still Phase 0 compliant: numeric, opaque, no meaning.
    """
    # Import here after path setup (intentional)
    from phase0.phase0 import phase0  # pylint: disable=import-outside-toplevel,import-error
    from phase0.actions import WeakOscillator  # pylint: disable=import-outside-toplevel,import-error

    # Oscillation is mechanical, not interpreted
    actions = [
        WeakOscillator(),
        WeakOscillator(),
    ]

    steps = 100  # Increased temporal depth to test persistence

    # Collect traces
    traces = []
    for trace, _, _ in phase0(actions, steps=steps):
        traces.append(trace)

    # Calculate canonical Phase 0 outputs ONLY
    total_count = len(traces)
    unique_count = len(set(traces))
    collision_rate = 1.0 - (unique_count / total_count) if total_count > 0 else 0.0

    # Output canonical Phase 0 results ONLY
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 0 (Oscillator Variant)")
    print("=" * 70)
    print()
    print("Total residue count:    ", total_count)
    print("Unique residue count:    ", unique_count)
    print("Collision rate:          ", f"{collision_rate:.4f}")
    print()
    print("=" * 70)

    return traces


def run_phase0_decay_noise():
    """
    Run Phase 0 pipeline — DECAY + NOISE VARIANT.
    
    Action decays with added noise.
    Still Phase 0 compliant: numeric, opaque, no meaning.
    """
    # Import here after path setup (intentional)
    from phase0.phase0 import phase0  # pylint: disable=import-outside-toplevel,import-error
    from phase0.actions import DecayNoise  # pylint: disable=import-outside-toplevel,import-error

    # Decay is mechanical, not interpreted
    actions = [
        DecayNoise(),
        DecayNoise(),
    ]

    steps = 100  # Increased temporal depth to test persistence

    # Collect traces
    traces = []
    for trace, _, _ in phase0(actions, steps=steps):
        traces.append(trace)

    # Calculate canonical Phase 0 outputs ONLY
    total_count = len(traces)
    unique_count = len(set(traces))
    collision_rate = 1.0 - (unique_count / total_count) if total_count > 0 else 0.0

    # Output canonical Phase 0 results ONLY
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 0 (Decay+Noise Variant)")
    print("=" * 70)
    print()
    print("Total residue count:    ", total_count)
    print("Unique residue count:    ", unique_count)
    print("Collision rate:          ", f"{collision_rate:.4f}")
    print()
    print("=" * 70)

    return traces


def run_phase0_finite():
    """
    Run Phase 0 pipeline — FINITE VARIANT.
    
    Actions output from a small finite set (discrete but meaningless).
    Still Phase 0 compliant: numeric, opaque, no meaning, no labels.
    
    Discreteness enables exact equality, allowing repetition to emerge naturally.
    """
    # Import here after path setup (intentional)
    from phase0.phase0 import phase0  # pylint: disable=import-outside-toplevel,import-error
    from phase0.actions import FiniteAction  # pylint: disable=import-outside-toplevel,import-error

    # Finite action with small output set (discrete but meaningless)
    actions = [
        FiniteAction(finite_set_size=10),  # Outputs 0-9
        FiniteAction(finite_set_size=10),  # Outputs 0-9
    ]

    steps = 100  # Increased temporal depth to test persistence

    # Collect traces
    traces = []
    for trace, _, _ in phase0(actions, steps=steps):
        traces.append(trace)

    # Calculate canonical Phase 0 outputs ONLY
    total_count = len(traces)
    unique_count = len(set(traces))
    collision_rate = 1.0 - (unique_count / total_count) if total_count > 0 else 0.0

    # Output canonical Phase 0 results ONLY
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 0 (Finite Variant)")
    print("=" * 70)
    print()
    print("Total residue count:    ", total_count)
    print("Unique residue count:    ", unique_count)
    print("Collision rate:          ", f"{collision_rate:.4f}")
    print()
    print("=" * 70)

    return traces


def run_phase1(residues):  # pylint: disable=redefined-outer-name
    """
    Run Phase 1 segmentation pipeline.
    
    Phase 1 performs segmentation without naming.
    Returns structural metrics only (numbers/indices).
    
    GATE: Phase 1 allowed to run only because Phase 0 is frozen.
    """
    # GATE CHECK: Phase 0 must be complete (frozen)
    if residues is None or len(residues) == 0:
        print("=" * 70)
        print("THRESHOLD_ONSET — Phase 1 GATE FAILED")
        print("=" * 70)
        print()
        print("Phase 1 not entered: Phase 0 must be frozen first")
        print()
        print("=" * 70)
        return None
    
    # Import here after path setup (intentional)
    from phase1.phase1 import phase1  # pylint: disable=import-outside-toplevel,import-error
    
    # Phase 1 segmentation
    metrics = phase1(residues)
    
    # Output Phase 1 results (FINAL outputs only, no stepwise logs)
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 1")
    print("=" * 70)
    print()
    print("Boundary positions:       ", metrics['boundary_positions'])
    print("Cluster count:            ", metrics['cluster_count'])
    print("Cluster sizes:            ", metrics['cluster_sizes'])
    print("Distance count:           ", len(metrics['distances']))
    print("Repetition count:         ", metrics['repetition_count'])
    print("Survival count:           ", metrics['survival_count'])
    print()
    print("=" * 70)
    
    return metrics


def run_phase2(residues, phase1_metrics):  # pylint: disable=redefined-outer-name
    """
    Run Phase 2 identity pipeline.
    
    Phase 2 performs identity detection without naming.
    Returns identity metrics only (hashes and counts).
    
    GATE: Phase 2 requires non-zero persistence indicators from Phase 1.
    """
    # GATE CHECK: Phase 1 must complete first
    if phase1_metrics is None:
        print("=" * 70)
        print("THRESHOLD_ONSET — Phase 2 GATE FAILED")
        print("=" * 70)
        print()
        print("Phase 2 not entered: Phase 1 must complete first")
        print()
        print("=" * 70)
        return None
    
    # GATE CHECK: Phase 1 must show indicators of potential persistence
    # If repetition and survival are both zero, Phase 2 cannot produce persistence
    repetition_count = phase1_metrics.get('repetition_count', 0)
    survival_count = phase1_metrics.get('survival_count', 0)
    
    if repetition_count == 0 and survival_count == 0:
        print("=" * 70)
        print("THRESHOLD_ONSET — Phase 2 GATE FAILED")
        print("=" * 70)
        print()
        print("Phase 2 not entered: no persistent identity detected")
        print("Repetition count:         ", repetition_count)
        print("Survival count:           ", survival_count)
        print()
        print("=" * 70)
        return None
    
    # Import here after path setup (intentional)
    from phase2.phase2 import phase2  # pylint: disable=import-outside-toplevel,import-error
    
    # Phase 2 identity detection
    identity_metrics = phase2(residues, phase1_metrics)
    
    # Output Phase 2 results (FINAL outputs only, no stepwise logs)
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 2")
    print("=" * 70)
    print()
    print("Persistence count:        ", len(identity_metrics['persistence_counts']))
    print("Persistent segments:      ", len(identity_metrics['persistent_segment_hashes']))
    print("Repeatability count:      ", len(identity_metrics['repeatability_counts']))
    print("Repeatable units:         ", len(identity_metrics['repeatable_unit_hashes']))
    print("Identity mappings:        ", len(identity_metrics['identity_mappings']))
    print("Identity persistence:     ", len(identity_metrics['identity_persistence']))
    print("Stability count:          ", len(identity_metrics['stability_counts']))
    print("Stable clusters:          ", len(identity_metrics['stable_cluster_hashes']))
    print()
    print("=" * 70)
    
    return identity_metrics


def run_phase2_multi_run(residue_sequences, phase1_metrics_list):  # pylint: disable=redefined-outer-name
    """
    Run Phase 2 identity pipeline with multiple runs.
    
    Tests persistence across multiple independent Phase 0 runs.
    Phase 2 performs identity detection without naming.
    Returns identity metrics only (hashes and counts).
    
    Args:
        residue_sequences: list of residue sequences (each from a separate Phase 0 run)
        phase1_metrics_list: list of Phase 1 metrics (one per run)
    """
    # Phase 2 gate check: only run if at least one Phase 1 run produced persistence
    has_persistence = any(
        metrics['repetition_count'] > 0 or metrics['survival_count'] > 0
        for metrics in phase1_metrics_list
    )
    
    if not has_persistence:
        print("=" * 70)
        print("THRESHOLD_ONSET — Phase 2 GATE FAILED (Multi-Run)")
        print("=" * 70)
        print()
        print("Phase 2 not entered: no persistent identity detected across runs")
        total_repetition = sum(m['repetition_count'] for m in phase1_metrics_list)
        total_survival = sum(m['survival_count'] for m in phase1_metrics_list)
        print("Total repetition count:    ", total_repetition)
        print("Total survival count:       ", total_survival)
        print()
        print("=" * 70)
        return None  # Refuse execution

    # Import here after path setup (intentional)
    from phase2.phase2 import phase2_multi_run  # pylint: disable=import-outside-toplevel,import-error

    # Phase 2 identity detection across multiple runs
    identity_metrics = phase2_multi_run(residue_sequences, phase1_metrics_list)

    # Output Phase 2 results (FINAL outputs only, no stepwise logs)
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 2 (Multi-Run)")
    print("=" * 70)
    print()
    print("Persistence count:        ", len(identity_metrics['persistence_counts']))
    print("Persistent segments:      ", len(identity_metrics['persistent_segment_hashes']))
    print("Repeatability count:      ", len(identity_metrics['repeatability_counts']))
    print("Repeatable units:         ", len(identity_metrics['repeatable_unit_hashes']))
    print("Identity mappings:        ", len(identity_metrics['identity_mappings']))
    print("Identity persistence:     ", len(identity_metrics['identity_persistence']))
    print("Stability count:          ", len(identity_metrics['stability_counts']))
    print("Stable clusters:          ", len(identity_metrics['stable_cluster_hashes']))
    print()
    print("=" * 70)

    return identity_metrics


def run_phase3(residues, phase1_metrics, phase2_metrics):  # pylint: disable=redefined-outer-name
    """
    Run Phase 3 relation pipeline.
    
    Phase 3 performs relation detection without naming.
    Returns relation metrics only (graph structures, counts, hash pairs).
    
    GATE: Phase 3 requires non-zero identities from Phase 2.
    """
    # GATE CHECK: Phase 2 must produce non-zero identities
    if phase2_metrics is None:
        print("=" * 70)
        print("THRESHOLD_ONSET — Phase 3 GATE FAILED")
        print("=" * 70)
        print()
        print("Phase 3 not entered: Phase 2 must complete with identities first")
        print()
        print("=" * 70)
        return None
    
    # Check for non-zero identities
    persistent_segments = len(phase2_metrics.get('persistent_segment_hashes', []))
    repeatable_units = len(phase2_metrics.get('repeatable_unit_hashes', []))
    identity_mappings = len(phase2_metrics.get('identity_mappings', []))
    
    # GATE CHECK: Must have non-zero identities
    if persistent_segments == 0 and repeatable_units == 0 and identity_mappings == 0:
        print("=" * 70)
        print("THRESHOLD_ONSET — Phase 3 GATE FAILED")
        print("=" * 70)
        print()
        print("Phase 3 not entered: no identities detected")
        print("Persistent segments:      ", persistent_segments)
        print("Repeatable units:         ", repeatable_units)
        print("Identity mappings:        ", identity_mappings)
        print()
        print("=" * 70)
        return None
    
    # Import here after path setup (intentional)
    from phase3.phase3 import phase3  # pylint: disable=import-outside-toplevel,import-error
    
    # Phase 3 relation detection
    relation_metrics = phase3(residues, phase1_metrics, phase2_metrics)
    
    # Output Phase 3 results (FINAL outputs only, no stepwise logs)
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 3")
    print("=" * 70)
    print()
    print("Node count:                ", relation_metrics['node_count'])
    print("Edge count:                 ", relation_metrics['edge_count'])
    print("Interaction pairs:          ", len(relation_metrics['interaction_pairs']))
    print("Dependency pairs:            ", len(relation_metrics['dependency_pairs']))
    print("Influence pairs:             ", len(relation_metrics['influence_counts']))
    print("Path length count:           ", len(relation_metrics['path_lengths']))
    print()
    print("=" * 70)
    
    return relation_metrics


def run_phase3_multi_run(residue_sequences, phase1_metrics_list, phase2_metrics):  # pylint: disable=redefined-outer-name
    """
    Run Phase 3 relation pipeline with multiple runs.
    
    Tests persistence and stability across multiple independent Phase 0 runs.
    Phase 3 performs relation detection without naming.
    Returns relation metrics only (graph structures, counts, hash pairs).
    
    Args:
        residue_sequences: list of residue sequences (each from a separate Phase 0 run)
        phase1_metrics_list: list of Phase 1 metrics (one per run)
        phase2_metrics: Phase 2 metrics from multi-run (aggregated)
    """
    # Import here after path setup (intentional)
    from phase3.phase3 import phase3_multi_run  # pylint: disable=import-outside-toplevel,import-error
    
    # Phase 3 multi-run relation detection
    relation_metrics = phase3_multi_run(residue_sequences, phase1_metrics_list, phase2_metrics)
    
    # Check if gate failed
    if relation_metrics is None:
        # Gate failed - need to compute values to show in failure message
        # Re-run Phase 3 multi-run to get diagnostic values (but don't use results)
        from phase3.relation import extract_relations  # pylint: disable=import-outside-toplevel,import-error
        from phase3.persistence import measure_relation_persistence  # pylint: disable=import-outside-toplevel,import-error
        from phase3.stability import measure_relation_stability  # pylint: disable=import-outside-toplevel,import-error
        from phase3.phase3 import phase3  # pylint: disable=import-outside-toplevel,import-error
        
        # Collect relations from all runs for diagnostics
        relation_hashes_per_run = []
        relation_counts_per_run = []
        graph_metrics_per_run = []
        
        for residues, phase1_metrics in zip(residue_sequences, phase1_metrics_list):  # pylint: disable=redefined-outer-name
            phase3_metrics_run = phase3(residues, phase1_metrics, phase2_metrics)  # pylint: disable=redefined-outer-name
            relation_result = extract_relations(phase3_metrics_run)
            relation_hashes_per_run.append(relation_result['relation_hashes'])
            relation_counts_per_run.append(relation_result['relation_counts'])
            graph_metrics_per_run.append({
                'node_count': phase3_metrics_run['node_count'],
                'edge_count': phase3_metrics_run['edge_count'],
                'graph_nodes': phase3_metrics_run['graph_nodes'],
                'graph_edges': phase3_metrics_run['graph_edges']
            })
        
        # Measure persistence and stability for diagnostics
        persistence_result = measure_relation_persistence(relation_hashes_per_run)
        persistent_relation_hashes = persistence_result['persistent_relation_hashes']
        persistent_relations = len(persistent_relation_hashes)
        persistence_rate = persistence_result['persistence_rate']
        
        stability_result = measure_relation_stability(
            relation_hashes_per_run,
            relation_counts_per_run,
            graph_metrics_per_run,
            persistent_relation_hashes
        )
        stability_ratio = stability_result['stability_ratio']
        
        # Get identity counts
        persistent_segments = len(phase2_metrics.get('persistent_segment_hashes', []))
        identity_mappings = len(phase2_metrics.get('identity_mappings', {}))
        persistent_identities = persistent_segments + identity_mappings
        
        # Output gate failure message with actual values
        print("=" * 70)
        print("THRESHOLD_ONSET — Phase 3 GATE FAILED")
        print("=" * 70)
        print()
        print("Phase 3 not entered: gate criteria not met")
        print()
        print("Gate Criteria:")
        print("  Persistent identities:      ", persistent_identities, " (required: > 0) [PASS]")
        print("  Persistent relations:       ", persistent_relations, " (required: >= 1)")
        print("  Stability ratio:            ", f"{stability_ratio:.4f}", " (required: >= 0.6)")
        print()
        print("Diagnostics:")
        print("  Total relations:            ", len(persistence_result['persistence_counts']))
        print("  Persistence rate:            ", f"{persistence_rate:.4f}")
        print("  Stable relations:           ", len(stability_result['stable_relation_hashes']))
        print("  Common edges ratio:         ", f"{stability_result['common_edges_ratio']:.4f}")
        print("  Edge density variance:      ", f"{stability_result['edge_density_variance']:.4f}")
        
        # Additional diagnostics: variance distribution
        from phase3.stability import STABILITY_VARIANCE_THRESHOLD  # pylint: disable=import-outside-toplevel,import-error
        variance_values = []
        for relation_hash in persistent_relation_hashes:
            occurrence_counts = []
            for relation_counts in relation_counts_per_run:
                count = relation_counts.get(relation_hash, 0)
                occurrence_counts.append(count)
            if len(occurrence_counts) > 1:
                mean_count = sum(occurrence_counts) / len(occurrence_counts)
                variance = sum((count - mean_count) ** 2 for count in occurrence_counts) / len(
                    occurrence_counts)
                variance_values.append(variance)
        
        if variance_values:
            import statistics  # pylint: disable=import-outside-toplevel
            print("  Variance stats (persistent relations):")
            print("    Mean variance:            ", f"{statistics.mean(variance_values):.4f}")
            print("    Median variance:          ", f"{statistics.median(variance_values):.4f}")
            print("    Max variance:             ", f"{max(variance_values):.4f}")
            stable_count = sum(1 for v in variance_values if v <= STABILITY_VARIANCE_THRESHOLD)
            unstable_count = sum(1 for v in variance_values if v > STABILITY_VARIANCE_THRESHOLD)
            print("    Relations with var <= 2.0:", stable_count)
            print("    Relations with var > 2.0: ", unstable_count)
        print()
        print("Note: Gate failure is expected if relations do not persist/stabilize.")
        print("This is correct behavior - Phase 3 must earn the right to freeze.")
        print()
        print("=" * 70)
        return None
    
    # Output Phase 3 results (FINAL outputs only, no stepwise logs)
    # CRITICAL: Output shows only counts, never hash values
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 3 (Multi-Run)")
    print("=" * 70)
    print()
    print("Node count:                ", relation_metrics['node_count'])
    print("Edge count:                 ", relation_metrics['edge_count'])
    print("Total relations:            ", len(relation_metrics['relation_hashes']))
    print("Persistent relations:       ", len(relation_metrics['persistent_relation_hashes']))
    print("Persistence rate:          ", f"{relation_metrics['persistence_rate']:.4f}")
    print("Stable relations:           ", len(relation_metrics['stable_relation_hashes']))
    print("Stability ratio:            ", f"{relation_metrics['stability_ratio']:.4f}")
    print("Common edges ratio:         ", f"{relation_metrics['common_edges_ratio']:.4f}")
    print("Path length count:           ", len(relation_metrics['path_lengths']))
    print()
    print("=" * 70)
    
    return relation_metrics


def run_phase4_multi_run(phase2_metrics, phase3_metrics):  # pylint: disable=redefined-outer-name
    """
    Run Phase 4 symbol pipeline (pure aliasing).
    
    Phase 4 creates reversible symbol mappings for persistent identities and relations.
    Phase 4 adds ZERO new structure - only aliases.
    
    Args:
        phase2_metrics: Phase 2 metrics from multi-run (aggregated)
        phase3_metrics: Phase 3 metrics from multi-run (aggregated, FROZEN)
    """
    # Import here after path setup (intentional)
    from phase4.phase4 import phase4  # pylint: disable=import-outside-toplevel,import-error
    
    # Phase 4 pure aliasing
    symbol_metrics = phase4(phase2_metrics, phase3_metrics)
    
    # Check if gate failed
    if symbol_metrics is None:
        # Gate failed - output failure message
        persistent_segments = len(phase2_metrics.get('persistent_segment_hashes', []))
        identity_mappings = len(phase2_metrics.get('identity_mappings', {}))
        persistent_identities = persistent_segments + len(identity_mappings)
        persistent_relations = len(phase3_metrics.get('persistent_relation_hashes', set()))
        
        print("=" * 70)
        print("THRESHOLD_ONSET — Phase 4 GATE FAILED")
        print("=" * 70)
        print()
        print("Phase 4 not entered: gate criteria not met")
        print()
        print("Gate Criteria:")
        print(f"  Phase 3 frozen:              {'[PASS]' if phase3_metrics is not None else '[FAIL]'}")
        print(f"  Persistent identities:      {persistent_identities}  (required: >= 1) {'[PASS]' if persistent_identities >= 1 else '[FAIL]'}")
        print(f"  Persistent relations:        {persistent_relations}  (required: >= 1) {'[PASS]' if persistent_relations >= 1 else '[FAIL]'}")
        print()
        print("Note: Gate failure is expected if Phase 3 is not frozen or prerequisites not met.")
        print("This is correct behavior - Phase 4 must earn the right to execute.")
        print()
        print("=" * 70)
        return None
    
    # Output Phase 4 results (FINAL outputs only, no stepwise logs)
    # CRITICAL: Output shows only counts, never symbol values
    print("=" * 70)
    print("THRESHOLD_ONSET — Phase 4 (Multi-Run)")
    print("=" * 70)
    print()
    print("Identity alias count:        ", symbol_metrics['identity_alias_count'])
    print("Relation alias count:        ", symbol_metrics['relation_alias_count'])
    print()
    print("=" * 70)
    
    return symbol_metrics


if __name__ == "__main__":
    # ========================================================================
    # CONFIGURATION
    # ========================================================================
    # Phase 0 Action Variants:
    # - "noise_baseline"     : Pure random (frozen baseline)
    # - "inertia"            : Temporal correlation
    # - "random_walk"        : Bounded random walk
    # - "oscillator"         : Bounded oscillator
    # - "decay_noise"        : Decay toward target + noise
    # - "finite"             : Discrete but meaningless (enables exact equality)
    # ========================================================================
    
    VARIANT = "finite"  # Select action variant
    MULTI_RUN_MODE = True  # Set to True for multi-run persistence testing
    NUM_RUNS = 5  # Number of independent Phase 0 runs (only used if MULTI_RUN_MODE = True)
    
    # ========================================================================
    # EXECUTION
    # ========================================================================
    
    if MULTI_RUN_MODE:
        # ====================================================================
        # MULTI-RUN MODE: Tests persistence across multiple independent runs
        # ====================================================================
        residue_sequences = []
        phase1_metrics_list = []
        
        for run_num in range(NUM_RUNS):
            # Run Phase 0 with selected variant
            if VARIANT == "noise_baseline":
                residues = run_phase0_noise_baseline()
            elif VARIANT == "inertia":
                residues = run_phase0_inertia()
            elif VARIANT == "random_walk":
                residues = run_phase0_random_walk()
            elif VARIANT == "oscillator":
                residues = run_phase0_oscillator()
            elif VARIANT == "decay_noise":
                residues = run_phase0_decay_noise()
            elif VARIANT == "finite":
                residues = run_phase0_finite()
            else:
                print(f"Unknown variant: {VARIANT}")
                print("Using noise_baseline")
                residues = run_phase0_noise_baseline()
            
            residue_sequences.append(residues)
            
            # Phase 1: GATED - only runs if Phase 0 is frozen
            phase1_metrics = run_phase1(residues)
            phase1_metrics_list.append(phase1_metrics)
        
        # Phase 2: MULTI-RUN - tests persistence across multiple runs
        phase2_metrics = run_phase2_multi_run(residue_sequences, phase1_metrics_list)
        
        # Phase 3: MULTI-RUN - tests relation persistence and stability across multiple runs
        # Gate will block execution if criteria not met
        phase3_metrics = None
        if phase2_metrics is not None and len(residue_sequences) > 0:
            phase3_metrics = run_phase3_multi_run(residue_sequences, phase1_metrics_list, phase2_metrics)
        
        # Phase 4: MULTI-RUN - pure aliasing (symbol assignment)
        # Gate will block execution if Phase 3 not frozen
        if phase2_metrics is not None and phase3_metrics is not None:
            run_phase4_multi_run(phase2_metrics, phase3_metrics)
    
    else:
        # ====================================================================
        # SINGLE-RUN MODE: Standard single execution
        # ====================================================================
        # Run Phase 0 with selected variant
        if VARIANT == "noise_baseline":
            residues = run_phase0_noise_baseline()
        elif VARIANT == "inertia":
            residues = run_phase0_inertia()
        elif VARIANT == "random_walk":
            residues = run_phase0_random_walk()
        elif VARIANT == "oscillator":
            residues = run_phase0_oscillator()
        elif VARIANT == "decay_noise":
            residues = run_phase0_decay_noise()
        elif VARIANT == "finite":
            residues = run_phase0_finite()
        else:
            print(f"Unknown variant: {VARIANT}")
            print("Using noise_baseline")
            residues = run_phase0_noise_baseline()
        
        # Phase 1: GATED - only runs if Phase 0 is frozen
        phase1_metrics = run_phase1(residues)
        
        # Phase 2: HARD-DISABLED - only runs if Phase 1 produces non-zero persistence
        phase2_metrics = run_phase2(residues, phase1_metrics)
        
        # Phase 3: HARD-DISABLED - only runs if Phase 2 produces non-zero identities
        if phase2_metrics is not None:
            run_phase3(residues, phase1_metrics, phase2_metrics)
