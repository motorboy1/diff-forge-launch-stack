# APPLY — gov__classify__risk_scoring_matrix__v1.0

## Prerequisites
- Ruby 3.0+

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Score an asset:**
   ```ruby
   meta = JSON.parse(File.read("assets/some_asset/META.json"))
   result = RiskScorer.new(meta).score
   puts "Risk: #{result[:band]} (#{result[:total_score]}/#{result[:max_possible]})"
   puts "Breakdown: #{result[:breakdown]}"
   ```

3. **Batch score all assets:**
   ```ruby
   Dir.glob("assets/*/META.json").each do |meta_path|
     meta = JSON.parse(File.read(meta_path))
     result = RiskScorer.new(meta).score
     puts "#{meta['asset_id']}: #{result[:band]} (#{result[:total_score]})"
   end
   ```

## Verification

1. Score a low-risk asset — should classify as `:low`
2. Score a high-risk security asset — should classify as `:high`
3. Verify breakdown adds up to total score

## Rollback

Delete `lib/risk_scorer.rb`.
